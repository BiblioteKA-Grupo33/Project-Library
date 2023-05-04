from django.shortcuts import get_object_or_404
from .models import Loans
from copys.models import Copy
from .serializers import LoansSerializer
from rest_framework import generics
import ipdb
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta

class LoansView(generics.ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

class LoansDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ]

    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

    def perform_create(self, serializer) -> None:
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])
        user = self.request.user
        
        if(user.can_borrow):
            serializer.save(copy=copy, user=user)
        else:
            raise TypeError
        

    def perform_update(self, serializer):
        borrowed_date = datetime.today()
        devolution_date = borrowed_date + timedelta(days=7)
        serializer.save(borrowed_date=borrowed_date, devolution_date=devolution_date)