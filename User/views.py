from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status


from django.core.mail import send_mail
from rest_framework.authtoken.models import Token


from .api.serializers import CreateUserSerializer
from User.models import User
from django.http import HttpResponse

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
            
            send_activation(account)
            
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
    

def send_activation(user):    
    send_mail(
        subject='Verify email',
        message=f'please click on the link to verify the account with username{user.username}\
                  {settings.CURRENT_DOMAIN}/user/{user.username}/verify/',
        from_email='a.b.mahdey@gmail.com',
        recipient_list=[f'{user.email}'],
        fail_silently=False)


@api_view(['GET', 'POST'])
def activate(request,username):
    user=User.objects.get(username=username)
    user.verify()
    user.save()

#     return Response({"Verified"})
    return HttpResponse("verified")
