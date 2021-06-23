from django.contrib import admin
from .models import Chamado
from .models import Usuario
from .models import Mensagem
from .models import Anexo
#Foi utilizada a primeira letra maiúscula para as classes importadas (ex: Usuário, Chamados ...)


admin.site.register(Chamado)
admin.site.register(Usuario)
admin.site.register(Mensagem)
admin.site.register(Anexo)

