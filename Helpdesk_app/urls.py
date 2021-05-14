from django.urls import path, include
from . import views


urlpatterns = [

path('', views.home, name ='home'),
path('chamados/', views.Chamado, name='chamados'),
path('login/', views.login_page, name='login'),
path('cadastro/', views.cadastro, name='cadastro')

]

