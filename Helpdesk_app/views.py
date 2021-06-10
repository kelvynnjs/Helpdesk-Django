#KELVYNN JOSÉ DA SILVA - IFPR - 2021

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



@login_required
def ver_chamado(request, id_chamado):
    chamados_si = obter_chamados()
    novs_cham = obter_novos_chamados()
    Usuario = request.user
    chamado = Chamado.objects.get(id=id_chamado)
    context = {}

    context['chamado'] = chamado
    context['Nome_Sistema'] = Nome_Sistema
    context['Novos_Chamados'] = novs_cham

    context['chamados'] = chamados_si

    return render(request,"chamado.html", context)


#Funções relacionadas à chamados

@login_required
def novo_chamado(request):
    context = {}

    if request.method == 'POST':

        usuario = request.user.nome_completo #Obtem o usuário do termo user dentro da request
        titulo_chamado = request.POST.get('titulo_chamado')
        texto_chamado = request.POST.get('texto_chamado')
        prioridade_chamado = request.POST.get('nivel_prioridade')
        topico_chamado = request.POST.get('topico_chamado')
        local_chamado = request.POST.get('local_chamado')

        print(titulo_chamado)

        nov_cham = Chamado.objects.create(autor = usuario, titulo = titulo_chamado, prioridade = prioridade_chamado, status = 'aberto', descricao = texto_chamado, local_afetado = local_chamado)
        nov_cham.save()
        messages.success(request,'Chamado aberto com successo')

        context['Nome_Sistema'] = Nome_Sistema
        return render(request, "painel.html", context)
    else:
        messages.info(request,'Utilize o painel para abrir um novo chamado')
        return HttpResponseRedirect(request,'home')


def obter_chamados():
    chamados_sis = Chamado.objects.all()

    return chamados_sis

def obter_novos_chamados(): #Obtem a query com todos os chamados que não foram lidos ainda
    chamados_novs = Chamado.objects.all().filter(foi_lido = False).count()  

    return chamados_novs

#   Listagem de chamados em suas categorias ------------------------------------------------------------

@login_required
def chamados_abertos(request):
    novs_cham = obter_novos_chamados()
    Usuario = request.user
    chamados_ab = Chamado.objects.all().filter(status='aberto')
    context = {}

    context['chamados'] = chamados_ab
    context['Novos_Chamados'] = novs_cham
    context['Nome_Sistema'] = Nome_Sistema
    context['filtro'] = 'abertos'

    return render(request, "painel.html", context)


@login_required
def chamados_excluidos(request):
    novs_cham = obter_novos_chamados()
    Usuario = request.user
    chamados_ex = Chamado.objects.all().filter(status='excluido')
    context = {}

    context['chamados'] = chamados_ex
    context['Novos_Chamados'] = novs_cham
    context['Nome_Sistema'] = Nome_Sistema
    context['filtro'] = 'excluidos'

    return render(request, "painel.html", context)



@login_required
def chamados_resolvidos(request):
    novs_cham = obter_novos_chamados()
    Usuario = request.user
    chamados_re = Chamado.objects.all().filter(status='resolvido')
    context = {}

    context['chamados'] = chamados_re
    context['Novos_Chamados'] = novs_cham
    context['Nome_Sistema'] = Nome_Sistema
    context['filtro'] = 'resolvidos'

    return render(request, "painel.html", context)

@login_required
def chamados_pendentes(request):
    novs_cham = obter_novos_chamados()
    Usuario = request.user
    chamados_pe = Chamado.objects.all().filter(status='pendente')
    context = {}

    context['chamados'] = chamados_pe
    context['Novos_Chamados'] = novs_cham
    context['Nome_Sistema'] = Nome_Sistema
    context['filtro'] = 'pendentes'

    return render(request, "painel.html", context)



@login_required
def painel(request):   #MOSTRA O PAINEL PRINCIPAL E TODOS OS CHAMADOS
    chamados_si = obter_chamados()
    novs_cham = obter_novos_chamados()
    Usuario = request.user

    context = {}
    
    context['Nome_Sistema'] = Nome_Sistema
    context['Novos_Chamados'] = novs_cham

    context['chamados'] = chamados_si
    context['filtro'] = 'todos'


    return render(request, "painel.html", context)


@login_required
def alterar_status(request):
    if request.method =='POST':
        status_novo = request.POST.get('selecionar_status')
        id_chamado = request.POST.get('id_chamado')
        o_chamado = Chamado.objects.get(id=id_chamado)
        o_chamado.status = status_novo
        o_chamado.save()
        messages.success(request,'Status do chamado Nº {} defino como {} com sucesso!'.format(id_chamado,status_novo.upper()))
        return redirect('/chamado/{}'.format(id_chamado),request)




@login_required
def alterar_prioridade(request):
    if request.method =='POST':
        prioridade_nova = request.POST.get('selecionar_prioridade')
        id_chamado = request.POST.get('id_chamado')
        o_chamado = Chamado.objects.get(id=id_chamado)
        o_chamado.prioridade = prioridade_nova
        o_chamado.save()



        messages.success(request,'Prioridade do chamado Nº {} defino como {} com sucesso!'.format(id_chamado,prioridade_nova.upper()))
        return redirect('/chamado/{}'.format(id_chamado),request)




# SEÇÃO DE USUARIOS
@login_required
def usuarios(request):
    context = {}
    usuarios = obter_usuarios()
    context['usuarios'] = usuarios
    chamados_si = obter_chamados()
    novs_cham = obter_novos_chamados()
    Usuario = request.user

    context['Nome_Sistema'] = Nome_Sistema
    context['Novos_Chamados'] = novs_cham

    context['chamados'] = chamados_si

    return render(request, "usuarios.html", context)


def obter_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def remover_usuario(nome_user):
    pass


