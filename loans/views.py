from django.shortcuts import get_object_or_404
from books.permission import IsAdminOrReadOnly
from loans.permissions import IsAdminOrLoanOwner
from .models import Loan
from copys.models import Copy
from .serializers import LoansSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta

import ipdb

class LoansView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,IsAdminOrReadOnly
    ]
    
    queryset = Loan.objects.all()
    serializer_class = LoansSerializer


class LoansAdminView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,IsAdminOrReadOnly
    ]

    queryset = Loan.objects.all()
    serializer_class = LoansSerializer
   
    def perform_update(self, serializer):
        loan = get_object_or_404(Loan, pk=self.kwargs["pk"])
        if(not loan.borrowed_date):
            borrowed_date = datetime.today()
            devolution_date = borrowed_date + timedelta(days=7)
            serializer.save(borrowed_date=borrowed_date, devolution_date=devolution_date)
        else:
            raise TypeError("ja emprestado")


class LoansUserView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrLoanOwner]

    queryset = Loan.objects.all()
    serializer_class = LoansSerializer

    def perform_create(self, serializer) -> None:
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])
        user = self.request.user

        if self.queryset.filter(copy=copy, is_devoluted=False):
            raise TypeError("ja emprestado")

        for borrowed in user.borroweds.all():
            today = datetime.today().date()
            if (
                not borrowed.is_devoluted
                and borrowed.devolution_date
                and today > borrowed.devolution_date.date()
            ):
                user.can_borrow = False
                user.save()

        if user.can_borrow:
            serializer.save(copy=copy, user=user)
        else:
            raise TypeError("não pode alugar")

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(is_devoluted = True)
        user.can_borrow = True
        user.save()
        