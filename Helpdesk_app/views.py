from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import HttpResponse, redirect, HttpResponseRedirect
from .forms import CadastrarUsuario
from .models import Chamado, Usuario
import datetime



# SÃO AS VISÕES DO APP


#Cria a pagina inicial

def home(request):

    context = {}
    return render(request, "home.html", context)



def cadastro(request):
        
        context = {}
        
        if request.method == 'POST':
            nome_usuario = request.POST.get('username')
            nome_comp = request.POST.get('nome_completo')
            email = request.POST.get('email')
            senha = request.POST.get('password')
            
            novo_user = Usuario.objects.create_user(username=nome_usuario, email=email, password=senha)
            novo_user.save(username=nome_usuario,nome_completo=nome_comp, email=email, password=senha)
            messages.success(request, 'Usuario {nome_usuario} cadastrado com sucesso ')

            return redirect('login')
        if request.method == 'GET':

            return render(request, 'cadastro.html', context)   	


def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username_log')
        password =request.POST.get('password_log')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)

            return redirect('home')
        else:
            messages.info(request, 'Usuário ou senha incorretos')
            
            
            context = {}
            return render(request, 'login.html', context)



    #else:
     #   messages.add_message(request, messages.ERROR)


    
def logout(request):
	logout(request)
	return redirect('login')




def chamados(request):
    context = {

    }
    return render(request, "chamados.html", context)


