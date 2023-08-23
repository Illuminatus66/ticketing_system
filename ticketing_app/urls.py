from django.urls import path
from django.shortcuts import redirect
from .views import admin_view, dashboard, auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('ticketing_app/register/', auth.register, name='register'),
    path('ticketing_app/login/', auth.user_login, name='login'),
    path('ticketing_app/dashboard/', dashboard.user_dashboard, name='user_dashboard'),
    path('ticketing_app/admin-view/', admin_view.admin_view, name='admin_view'),
    path('ticketing_app/logout/', auth_views.LogoutView.as_view(), name='logout')
]
