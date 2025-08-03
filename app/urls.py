from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('farm/', views.farm, name='farm'),
    path('irrigation/', views.irrigation, name='irrigation'),
    path('pesticides/', views.pesticides, name='pesticides'),
    path('fertilizers/', views.fertilizers, name='fertilizers'),
]