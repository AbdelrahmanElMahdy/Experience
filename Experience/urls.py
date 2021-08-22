from django.urls import path,include
from .views import ExpList,CreateExp,RemoveExp,ExpUpdate

app_name="experience"

urlpatterns = [
    path("list/",ExpList.as_view(),name='list'),
    path("createexp/",CreateExp.as_view(),name='CreateExp'),
    path("ExpUpdate/<int:pk>/",ExpUpdate.as_view(),name='ExpUpdate'),
    path("ExpRateList/<int:pk>/",ExpRateList.as_view(),name='ExpRateList'),
    path("CreateRate/<int:pk>/",CreateRate.as_view(),name='CreateRate'),
    path("RemoveRate/<int:pk>/",RemoveRate.as_view(),name='RemoveRate'),
    path("RateUpdate/<int:pk>/",RateUpdate.as_view(),name='RateUpdate'),

]
