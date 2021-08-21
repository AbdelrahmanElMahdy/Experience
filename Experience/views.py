from django.shortcuts import render
from rest_framework import generics
from .models import Experience
from .serializers import CreatExpSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
# Create your views here.

class ExpList(generics.ListAPIView):
    queryset=Experience.objects.all()
    serializer_class=CreatExpSerializer
    permission_classes = [IsAuthenticated]

class CreateExp(generics.CreateAPIView):
    queryset=Experience.objects.all()
    serializer_class=CreatExpSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)