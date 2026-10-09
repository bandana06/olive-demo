from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('complain/', views.complain, name='complain'),
    path('wheel/', views.wheel, name='wheel'),
]
