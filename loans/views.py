from django.shortcuts import get_object_or_404
from .models import Loans
from books.models import Book
from .serializers import LoansSerializer
from rest_framework import generics

class LoansView(generics.ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

class LoansDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

    def perform_create(self, serializer) -> None:
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book, user=self.request.user)
