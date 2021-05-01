from django.db import models
from django.conf import settings
from django.utils import timezone




# Tabela de Chamados.
class Chamados(models.Model):
    autor = models.CharField(max_length=45)
    prioridade = models.CharField(max_length=30)
    chamado_titulo = models.CharField(max_length=30)
    chamado_tipo = models.CharField(max_length=30)
    chamado_corpo = models.TextField()
    data_hora_abertura = models.DateTimeField()



""" class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length=45)
    email_usuario = models.CharField(max_length=45)
    departamento_usuario = models.CharField(max_length=75)

 """