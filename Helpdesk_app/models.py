from django.db import models
from django.conf import settings
from django.utils import timezone




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

""" class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length=45)
    email_usuario = models.CharField(max_length=45)
    departamento_usuario = models.CharField(max_length=75)

 """