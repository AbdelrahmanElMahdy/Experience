from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework import status


from .models import Experience
from .serializers import CreatExpSerializer
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

class RemoveExp(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        expInstance=Experience.objects.filter(pk=self.kwargs['pk'])
        return expInstance
    

    def destroy(self, request, *args, **kwargs):
        try:
            instance=self.get_queryset()[0]
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

        
        if self.request.user==instance.author:
            instance.delete()
        
        else:
            return Response("unauthorized operation",status=status.HTTP_401_UNAUTHORIZED)
            