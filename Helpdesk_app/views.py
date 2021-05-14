from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, redirect
from .models import Chamado
import datetime



# Create your views here.  SÃO AS VISÕES DO APP


#Cria a pagina inicial

def home(request):

    context = {}
    return render(request, "home.html", context)


def login_page(request):
    context = {}
    return render(request, "login.html", context)
"""     if request.method == 'GET':
        return render(request, "login.html", context)
    if request.method == 'POST':
        
    else: """
    
def chamados(request):
    context = {

    }
    return render(request, "chamados.html", context)


def cadastro(request):
    context = {"form": UsuarioForm}

    return render(request, "cadastro.html", context)

def cadastrar_usuario(request):
    form = UsuarioForm(request.POST)
    if form.is_valid:
        cadastro = Usuario(
            nome_usuario = form.cleaned_data['nome_usuario'],
            nome_completo = form.cleaned_data['nome_completo'],
            email = form.cleaned_data['email'],
            senha_usuario = form.cleaned_data['senha_usuario'],
            data_criacao = datetime.datetime.now(),
        
    
        )
        cadastro.save()

        return redirect('home')