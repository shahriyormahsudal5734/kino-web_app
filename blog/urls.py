from .views import *
from django.urls import path

urlpatterns = [

    path('',Homepage.as_view() , name='home'),
    path('kino/<int:pk>', Homedetail.as_view(), name="kino"),
    path('update/<int:pk>', Homeupdate.as_view(), name="updatekino"),
    path('delete/<int:pk>', Homedel.as_view(), name="delkino"),
]
