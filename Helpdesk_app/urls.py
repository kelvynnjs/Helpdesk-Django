from django.urls import path, include
from . import views


urlpatterns = [

path('', views.home, name ='home'),
path('chamados/', views.Chamado, name='chamados'),
path('login/', views.login, name='login'),
path('cadastro/', views.cadastro, name='cadastro'),
path('usuarios/', views.usuarios, name='usuarios'),
path('painel/', views.painel, name='painel'), #todos os chamados
path('painel/abertos', views.chamados_abertos, name='chamados_abertos'), #chamados abertos
path('painel/excluidos', views.chamados_excluidos, name='chamados_excluidos'),#chamados excluidos
path('painel/resolvidos', views.chamados_resolvidos, name='chamados_resolvidos'), #chamados resolvidos
path('painel/pendentes', views.chamados_pendentes, name='chamados_pendentes'), #chamados resolvidos

path('alterar_status/', views.alterar_status, name='alterar_status'), 
path('alterar_prioridade/', views.alterar_prioridade, name='alterar_prioridade'), 

path('ler_chamado/', views.ler_chamado, name='ler_chamado'), 


path('sair/', views.sair, name='sair'),
path('novo_chamado/', views.novo_chamado, name='novo_chamado'),
path('chamado/<int:id_chamado>', views.ver_chamado, name='ver_chamado'),





]

