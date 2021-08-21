from django.urls import path,include
from .views import ExpList,CreateExp

app_name="experience"

urlpatterns = [
    path("list/",ExpList.as_view(),name='list'),
    path("createexp/",CreateExp.as_view(),name='CreateExp')

]
