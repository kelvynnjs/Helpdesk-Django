from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('', views.home, name ='home'),
path('chamados/', views.Chamado, name='chamados'),
path('login/', views.login, name='login'),
path('cadastro/', views.cadastro, name='cadastro'),
path('usuarios/', views.usuarios, name='usuarios'),
path('painel/', views.painel, name='painel'), #todos os chamados
path('painel/abertos', views.chamados_abertos, name='chamados_abertos'), #chamados abertos
path('painel/fechados', views.chamados_fechados, name='chamados_fechados'),#chamados fechados
path('painel/resolvidos', views.chamados_resolvidos, name='chamados_resolvidos'), #chamados resolvidos
path('painel/pendentes', views.chamados_pendentes, name='chamados_pendentes'), #chamados pendentes


path('alterar_status/', views.alterar_status, name='alterar_status'), 
path('alterar_prioridade/', views.alterar_prioridade, name='alterar_prioridade'), 
path('excluir_chamados/', views.excluir_chamados, name='excluir_chamados'), 

path('ler_chamado/', views.ler_chamado, name='ler_chamado'), 


path('sair/', views.sair, name='sair'),
path('novo_chamado/', views.novo_chamado, name='novo_chamado'),
path('chamado/<int:id_chamado>', views.ver_chamado, name='ver_chamado'),

#EXTRA
path('upload_anexo/', views.upload_anexo, name='upload_anexo')

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)