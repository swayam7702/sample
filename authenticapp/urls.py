from django.urls import path
from .views import home,login,sample,signup,about
urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('sample',sample,name="sample"),
]
