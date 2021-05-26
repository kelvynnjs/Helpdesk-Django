#KELVYNN JOSÉ DA SILVA - IFPR - 2021
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser



#Foi utilizada a primeira letra maiúscula para as classes importadas (ex: Usuário, Chamados ...)

# Tabela de Chamados.
class Chamado(models.Model):
    autor = models.CharField(max_length=45)
    prioridade = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    topico = models.CharField(max_length=30)
    corpo = models.TextField()
    data_hora_abertura = models.DateTimeField()

    def __str__(self):
        return self.titulo
    #Status do chamado ex: ABERTO, CONCLUÍDO, DELETADO 
    #prioridade é o nível de prioridade ex: ALTA, MEDIA, BAIXA
    #Tópico (ex: Dificuldade de acesso; Solicitar Instalação; Problemas com o computador)


#------------------------------------SOFRIMENTO--------------------------------------#
class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=60) # nome completo do usuário
    data_criacao = models.DateTimeField(auto_now_add=True) #data de criação do usuário
    data_modificacao = models.DateTimeField(auto_now=True) #data de modificação do usuário

#-----------------------------------FIM_SOFRIMENTO------------------------------------#


