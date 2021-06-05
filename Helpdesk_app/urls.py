from django.urls import path, include
from . import views


urlpatterns = [

path('', views.home, name ='home'),
path('chamados/', views.Chamado, name='chamados'),
path('login/', views.login, name='login'),
path('cadastro/', views.cadastro, name='cadastro'),
path('usuarios/', views.usuarios, name='usuarios'),
path('painel/', views.painel, name='painel'),
path('sair/', views.sair, name='sair'),
path('novo_chamado/', views.novo_chamado, name='novo_chamado'),
path('chamados/<int:id_chamado>', views.ver_chamado, name='ver_chamado'),





]

