#KELVYNN JOSÉ DA SILVA - IFPR - 2021

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser



#Foi utilizada a primeira letra maiúscula para as classes importadas (ex: Usuário, Chamados ...)



#Campos que não são explicitamente citados como "Null = True" são "NOT Null", ou seja, exigem algum valor necessariamente
#pelo sistema

#De maneira oculta, todos as tabelas no banco de dados incluem um campo "ID" unico por padrão, não sendo assim
#necessária a declaração dentro do escopo de 'models'

#Algumas foreign keys são utilizadas





class Chamado(models.Model):
    OPCOES_PRIORIDADE = [

     ('alta', 'Alta'),
     ('media', 'Media'),
     ('baixa', 'Baixa')]

    OPCOES_STATUS = [

     ('aberto', 'Aberto'),
     ('resolvido', 'Resolvido'),
     ('pendente', 'Pendente'),
     ('fechado', 'Fechado'),
     ('excluido', 'Excluido') ]



    autor = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    prioridade = models.CharField(max_length=30, choices=OPCOES_PRIORIDADE)
    agente_atribuido = models.CharField(max_length=100, default = None, null=True) # Não será usado foreign Key, #pois caso um usuário seja deletado, o nome continuará no banco de dados 
    status = models.CharField(max_length=30, choices=OPCOES_STATUS) #Status do chamado ex: ABERTO, CONCLUÍDO...
    titulo = models.CharField(max_length=50)
    topico = models.CharField(max_length=50) #Tópico (ex: Dificuldade de acesso; Solicitar Instalação; Problemas com o computador)
    descricao = models.TextField()
    local_afetado = models.CharField(max_length=50, default=None) #Local onde a pessoa se encontra
    hora_abertura = models.DateTimeField(auto_now_add=True) #Hora de criação do chamado
    foi_lido = models.BooleanField(default=False) #Define se o chamado já foi lido por um atendente
  
    



    def __str__(self):
        return self.titulo
    #Status do chamado ex: ABERTO, CONCLUÍDO, DELETADO 
    #prioridade é o nível de prioridade ex: ALTA, MEDIA, BAIXA
    #Tópico (ex: Dificuldade de acesso; Solicitar Instalação; Problemas com o computador)


#------------------------------------usuario--------------------------------------#
class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=120) # nome completo do usuário
    data_criacao = models.DateTimeField(auto_now_add=True) #data de criação do usuário
    data_modificacao = models.DateTimeField(auto_now=True) #data de modificação do usuário
    is_atendente = models.BooleanField(default=False) #Define se o usuário é um atendente ou não
    
    def __str__(self):
        return self.username


#-----------------------------------FIM_usuario------------------------------------#


class Mensagem(models.Model): 
    autor_mensagem = models.ForeignKey('Usuario', related_name='autor_mensagem', on_delete=models.CASCADE) # quem escreve a mensagem
    hora_mensagem = models.DateTimeField(auto_now_add=True) # HORA QUE A MENSAGEM FOI ENVIADA 
    texto = models.TextField() #texto da mensagem
    receptor_mensagem = models.ForeignKey('Usuario',related_name='receptor_mensagem',on_delete=models.CASCADE) # quem recebe a mensagem


#Anexo
class Anexo(models.Model):
    titulo = models.CharField(max_length=50)
    local = models.CharField(max_length=150)
    arquivo = models.FileField()
