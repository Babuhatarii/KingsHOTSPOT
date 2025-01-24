from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('access_granted/', views.access_granted, name='access_granted'),
]
