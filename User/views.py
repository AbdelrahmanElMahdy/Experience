from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from rest_framework.authtoken.models import Token


from .api.serializers import CreateUserSerializer

# Create your views here.

def index(request):
    return render(request,"Base.html")

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def createAccount(request):
    serializer=CreateUserSerializer(data=request.data)
    response={}

    if request.method=="POST":
        if serializer.is_valid():
            account=serializer.save()
            
            response['account_details']={
                'email':account.email,
                'Token':Token.objects.get(user=account).key,
                'date_created':account.date_created
                }

        else:
            response['errors']=serializer.errors

    else:
        response["required fields"]=[
            "email",
            "username"
            "password",
            "password2",
            ]
        response["optional fields"]=[
            "first_name",
            "lasr_name"
        ]
        
    return Response( response )
    
