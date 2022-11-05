from django.urls import path
from .import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('customer_dashboard',views.customerDashboard, name='customer_dashboard'),

]