from django.urls import path
from django.http import HttpResponse,HttpResponseRedirect
from . import views

urlpatterns = [
    path('',views.backtesting,name='backtesting'),
    #path('', views.index, name='main_index'),
]