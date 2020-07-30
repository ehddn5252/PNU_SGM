from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.start, name='main_start'),
    path('index', views.index, name='main_index'),
    path('signup', views.signup, name='main_signup'),
    path('signup/join', views.join, name='main_join'),
    path('signin', views.signin, name='main_signin'),
    path('signin/login', views.login, name='main_login'),
    path('loginFail', views.loginFail, name='main_loginFail'),
    path('verifyCode', views.verifyCode, name='main_verifyCode'),
    path('result', views.result, name='main_result'),
    path('logout', views.logout, name='main_logout'),
    path('explain1', views.explain1, name='main_explain1'),
    path('explain2', views.explain2, name='main_explain2'),
    path('explain3', views.explain3, name='main_explain3'),
    
]
