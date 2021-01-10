from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('Home', views.Home, name='ArmySensor'),
    path('league_stats', views.league_stats,name='league'),
    path('pre', views.Home,name='pre'),
    path('green', views.green,name='pre'),
    path('yellow', views.yellow,name='pre'),
    path('red', views.red,name='pre'),
    path('detect', views.detect, name='detect'),
    path('Login_re', views.Login_re, name='Login_re'),
    path('restart', views.restart, name='restart'),
    path('timeset', views.timeset, name='timeset'),
    path('saved', views.saved, name='saved'),
    path('popup', views.popup, name='popup'),
    path('center', views.center, name='center'),
    path('center_2', views.center_2, name='center'),
    path('center_3', views.center_3, name='center_2'),
    path('center_4', views.center_4, name='center_3'),
    path('mountain', views.mountain, name='mountain'),
]