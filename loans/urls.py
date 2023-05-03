from django.urls import path
from . import views

urlpatterns = [
    path("loans/", views.LoansView.as_view()),
    path("loans/<int:pk>/", views.LoansDetailView.as_view())

]