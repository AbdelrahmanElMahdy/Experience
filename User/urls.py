from django.urls import path

from rest_framework.authtoken import views


from .views import createAccount,index,activate,change_password

app_name="user"

urlpatterns = [
    path('',index,name='index'),
    path('signup/', createAccount ,name="sinup"),
    path('login/', views.obtain_auth_token,name='login'),
    path("<str:username>/verify/",activate,name='activate'),
    path('change_password/', change_password,name='login')

]
