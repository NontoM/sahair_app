from django.urls import path
from . import views


urlpatterns = [
    path('customer_register/', views.customerRegisterView, name="customer_register" ),
    #path('register_auth/', views.customerRegisterAuth, name="register_auth" ),

    path('login/',views.loginView, name='login'),
    #path('login_auth/',views.loginAuthView, name='login_auth'),

    #path('user_profile/',views.user_profileView, name='user_profile'),
    path('logout/', views.log_out, name='logout'),


]