from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, redirect
from .models import Chamado



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
    context = {}

    return render(request, "cadastro.html", context)