from django.contrib import admin
from . models import Chamado
from .models import Usuario
#Foi utilizada a primeira letra maiúscula para as classes importadas (ex: Usuário, Chamados ...)


admin.site.register(Chamado)
admin.site.register(Usuario)

