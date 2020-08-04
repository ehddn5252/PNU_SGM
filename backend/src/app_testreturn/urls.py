from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTestReturn.as_view()),
    path('<int:pk>/', views.DetailTestReturn.as_view()),
]