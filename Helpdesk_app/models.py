#KELVYNN JOSÉ DA SILVA - IFPR - 2021

from django.db import models
from django.conf import settings
from django.utils import timezone


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

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)  #nome do usuário
    nome_completo = models.CharField(max_length=60) # nome completo do usuário
    senha_usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=100) #email do usuário
    place = models.CharField(max_length=45) #departamento/local onde o usuário solicitante se encontra (onde o suporte acontece)
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False, blank=False) #data de criação do usuário

    def __str__(self):
        return self.nome_completo




