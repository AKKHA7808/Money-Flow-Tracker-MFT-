from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        form_class=CustomLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.public_password_reset, name='forgot_password'),
    path('', views.dashboard, name='dashboard'),
    path('api/cashflow-data/', views.get_cashflow_data, name='get_cashflow_data'),
]
