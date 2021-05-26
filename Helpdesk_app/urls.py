from django.urls import path, include
from . import views


urlpatterns = [

path('', views.home, name ='home'),
path('chamados/', views.Chamado, name='chamados'),
path('login/', views.login, name='login'),
path('cadastro/', views.cadastro, name='cadastro'),
path('404/', views.erro_404, name='404'),



]

