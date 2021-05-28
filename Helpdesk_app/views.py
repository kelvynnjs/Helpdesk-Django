from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, HttpResponseRedirect
from .forms import CadastrarUsuario
from .models import Chamado, Usuario
import datetime


# SÃO AS VISÕES DO APP





#VARIAVEIS e CONSTANTES


Nome_Empresa = 'Instituto Federal do Paraná' # Define o Nome da Empresa

Nome_Sistema = 'Helpdesk - {}'.format(Nome_Empresa) # Define o Nome do Sistema



#



#Cria a pagina inicial
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/painel/")
    else:
        context = {}
        context['Nome_Sistema'] = Nome_Sistema
        return render(request, "home.html", context)



def cadastro(request):
        
        context = {}
        context['Nome_Sistema'] = Nome_Sistema
        if request.method == 'GET':

            return render(request, 'cadastro.html', context)   	

        if request.method == 'POST':
         
            try:
                usuario_nome = Usuario.objects.get(username=request.POST.get('username'))
                usuario_email = Usuario.objects.get(email=request.POST.get('email'))
                if usuario_nome or usuario_email: #verifica se o nome de usuario já existe
                    messages.error(request,'Esse usuário já existe')
                    redirect('cadastro')
                    
            except Usuario.DoesNotExist:
                nome_usuario = request.POST.get('username')
                nome_comp = request.POST.get('nome_completo')
                email = request.POST.get('email')
                senha = request.POST.get('password')
        
                novo_user = Usuario.objects.create_user(username=nome_usuario, email=email, password=senha, nome_completo = nome_comp)
                novo_user.save()
                messages.success(request,'Usuario {} cadastrado com sucesso '.format(nome_usuario)) #Cria o usuario

                return redirect(request, 'cadastro')
       

            
        
        else:
            return render(request, 'cadastro.html', context)   	





def login(request):

    context = {}

    if request.method == 'POST':
        usuario_log = Usuario.objects.get(username=request.POST['username'])
        usuario = authenticate(username=usuario_log.username,password=request.POST["password"])
        
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('painel')
            #return HttpResponseRedirect('')

        else:
            
            messages.warning(request, 'Usuário ou senha incorretos')

            #return HttpResponseRedirect('home')

            return redirect('home')

    else:
        
        context = {}
        context['Nome_Sistema'] = Nome_Sistema
        return render(request, 'login.html', context)


    #''DESLOGA O USUÁRIO''
@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/')


def erro_404(request):
    return render(request, '404.html')




def chamados(request):
    context = {}
    context['Nome_Sistema'] = Nome_Sistema
    return render(request, "chamados.html", context)


def painel(request):
    context = {}
    context['Nome_Sistema'] = Nome_Sistema
    return render(request, "painel.html", context)




