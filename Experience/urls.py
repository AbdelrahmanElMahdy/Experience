from django.urls import path,include
from .views import ExpList,ExpById,CreateExp,RemoveExp,ExpUpdate,ExpRateList,CreateRate,RemoveRate,RateUpdate

app_name="experience"

urlpatterns = [
    path("createexp/",CreateExp.as_view(),name='CreateExp'),
    path("list/<int:pk>/",ExpById.as_view(),name='ExpById'),
    path("list/",ExpList.as_view(),name='list'),
    path("ExpUpdate/<int:pk>/",ExpUpdate.as_view(),name='ExpUpdate'),
    path("RemoveExp/<int:pk>/",RemoveExp.as_view(),name='RemoveExp'),
    path("ExpRateList/<int:pk>/",ExpRateList.as_view(),name='ExpRateList'),
    path("CreateRate/<int:pk>/",CreateRate.as_view(),name='CreateRate'),
    path("RemoveRate/<int:pk>/",RemoveRate.as_view(),name='RemoveRate'),
    path("RateUpdate/<int:pk>/",RateUpdate.as_view(),name='RateUpdate'),

]
