from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Follow
from .serializer import FollowsSerializer

# Create your views here.


class FollowView(CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowsSerializer
    lookup_url_kwarg = "pk"
