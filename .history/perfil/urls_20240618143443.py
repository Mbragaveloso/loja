from django.urls import path
from . import views
from .forms_perfil import PerfilForm, UserForm

app_name = 'perfil'

urlpatterns = [
    path('', views.CriarPerfilView.as_view(), name='criar'),  # Corrigido para CriarPerfilView
    path('atualizar/', views.Atualizar.as_view(), name='atualizar'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]