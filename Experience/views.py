from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework import status


from .models import Experience
from .serializers import CreatExpSerializer,ListExpSerializer, UpdateExpSerializer
# Create your views here.

class ExpList(generics.ListAPIView):
    queryset=Experience.objects.all()
    serializer_class=ListExpSerializer
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

# class DetailExp(generics.)

class ExpUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=UpdateExpSerializer

    def get_queryset(self):
        return Experience.objects.filter(pk=self.kwargs['pk'])
             

    
    def update(self, request, *args, **kwargs):
        try:
            instance=self.get_queryset()[0]
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)


        if self.request.user==instance.author:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(instance)
            
            return Response(serializer.data,status=status.HTTP_200_OK)

        else:
            return Response("unauthorized operation",status=status.HTTP_401_UNAUTHORIZED)

#list all rate for specific experience

class ExpRateList(generics.ListAPIView):
    serializer_class=ExpRateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset=Rate.objects.filter(
                experience=Experience.objects.filter(
                           id=self.kwargs['pk'])[0]
                )
        return queryset



