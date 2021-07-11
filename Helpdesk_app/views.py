#KELVYNN JOSÉ DA SILVA - IFPR - 2021

from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CadastrarUsuario
from django.http import JsonResponse
from .models import Chamado, Usuario, Anexo, Mensagem, Anexos_chamado
import datetime
import time


def obter_notificacoes (request): #OBTEM NOVOS CHAMADOS DE MANEIRA ASSÍNCRONA USANDO AJAX
	
	novos_chamados = obter_novos_chamados()
	#novas_mensagens = obter_novas_mensagens()
	data = {'novos_chamados': novos_chamados}

	return JsonResponse(data)




# SÃO AS VISÕES DO APP



#VARIAVEIS e CONSTANTES


Nome_Empresa = 'Instituto Federal do Paraná' # Define o Nome da Empresa

Nome_Sistema = 'Helpdesk - {}'.format(Nome_Empresa) # Define o Nome do Sistema


#Cria a pagina inicial do usuario "PAINEL DO USUARIO"
def home(request):
	context = {}
	context['Nome_Sistema'] = Nome_Sistema
	if request.user.is_authenticated:
		if request.user.is_atendente == True:
			return HttpResponseRedirect("/painel/")
		else:
			
			usuario = request.user
			#usuario = request.user
			chamados_usuario = Chamado.objects.all().filter(autor_id = usuario.id)
			context['chamados_usuario'] = chamados_usuario


			return render(request,"home.html",context)

			
	else:
		
		return render(request,"home.html",context)


#Página de Configurações
@login_required
def config(request):
	context = {}
	chamados_si = obter_chamados()
	novs_cham = obter_novos_chamados()
	context = {}



	context['Nome_Sistema'] = Nome_Sistema

	context['Nome_Empresa'] = Nome_Empresa

	context['Novos_Chamados'] = novs_cham

	context['chamados'] = chamados_si




	

	if request.user.is_authenticated:
		if request.user.is_atendente == True:
			return render(request, "UI/configuracoes.html", context)




		else:


			return render(request,"home.html",context)













#CADASTRO DE USUÁRIO

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

				return redirect('login')
	   

			
		
		else:
			return render(request, 'cadastro.html', context)   	





def login(request):

	context = {}

	if request.method == 'POST':
		usuario_log = Usuario.objects.get(username=request.POST['username'])
		usuario = authenticate(username=usuario_log.username,password=request.POST["password"])
		
		if usuario is not None:
			auth_login(request, usuario)
			usuario_nivel = Usuario.objects.get(username=request.POST.get('username'))

			if usuario_nivel.is_atendente == True:
				
				return redirect('painel')
				messages.success(request,'Usuário {} logado com sucesso'.format(usuario_nivel))
				#return HttpResponseRedirect('')
			else:
				return redirect('home')
				messages.success(request,'Usuário {} logado com sucesso'.format(usuario_nivel))

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
	messages.info(request, 'Você Saiu com sucesso')
	return HttpResponseRedirect('/')








#LEITURA INDIVIDUAL DOS CHAMADOS
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

	anexos = Anexos_chamado.objects.all().filter(chamado=chamado)


	context['anexos'] = anexos

	return render(request,"chamado.html", context)





#MARCA CHAMADO COMO "LIDO, E RETIRA A TAG 'NOVO'
@login_required
@csrf_exempt
def ler_chamado(request):

	if request.is_ajax() and request.method =='POST':

		id_lido = request.POST.getlist('id_chamado[]')
		foi_lido = request.POST.get('foi_lido')

		for id_un in id_lido:
				
			Chamado_ler_un = Chamado.objects.get(id=id_un)
			Chamado_ler_un.foi_lido = foi_lido
			Chamado_ler_un.save()
			print('chamado {} lido foi marcado como {}'.format(id_un,foi_lido))


		return(HttpResponse('success'))
			

	else:
		print('não é ajax')
		return(HttpResponse,'haha')




#Funções relacionadas à chamados

@login_required
def novo_chamado(request):
	context = {}

	if request.method == 'POST':

		usuario = request.user #.nome_completo #Obtem o usuário do termo user dentro da request
		titulo_chamado = request.POST.get('titulo_chamado')
		texto_chamado = request.POST.get('texto_chamado')
		prioridade_chamado = request.POST.get('nivel_prioridade')
		topico_chamado = request.POST.get('topico_chamado')
		local_chamado = request.POST.get('local_chamado')

	

		nov_cham = Chamado.objects.create(autor = usuario, titulo = titulo_chamado, prioridade = prioridade_chamado, status = 'aberto', descricao = texto_chamado, local_afetado = local_chamado, topico = topico_chamado)
		nov_cham.save()
		messages.success(request,'Chamado aberto com successo')

		context['Nome_Sistema'] = Nome_Sistema

		if usuario.is_atendente == True:
			return render(request, "painel.html", context)
				

		else:
			return render(request, "home.html", context)
	else:
		messages.info(request,'Utilize o painel para abrir um novo chamado')
		return HttpResponseRedirect(request,'home')


def obter_chamados(): #Lembrar de obter chamados usando essa função para evitar chamados com status excluído
	chamados_sis = Chamado.objects.all().exclude(status='excluido')

	return chamados_sis

def obter_novos_chamados(): #Obtem a query com todos os chamados que não foram lidos ainda
	chamados_novs = Chamado.objects.all().filter(foi_lido = False).count()  

	return chamados_novs

@login_required
@csrf_exempt
def excluir_chamados(request): #Exclue os chamados selecionados
	if request.is_ajax == True and request.method == 'POST':
	
		ids_lidos = request.POST.getlist('id_chamado[]')

		for id_un in ids_lidos:
				
			Chamado_ler_un = Chamado.objects.get(id=id_un)

			Chamado_ler_un.delete()
			messages.info(request,f'Os chamados {ids_lidos} foram excluidos com sucesso')


		return(HttpResponse('success'))
	if request.method == 'POST' and request.is_ajax == False:
			chamado_id = request.POST.get('id_chamado')
			Chamado.objects.get(id=chamado_id).delete()
			messages.info(request,'Chamado {} excluido com sucesso'.format(chamado_id))
			

	else:
		id_un = request.POST.getlist('id_chamado')[0]
		chamado_excluir = Chamado.objects.get(id=id_un)
		chamado_excluir.delete()
		messages.info(request,f'O chamado {str(id_un)} foi excluído com sucesso')
		if request.user.is_atendente == True:
			return redirect('painel')
		else:
			return redirect('home')


			
		







#   Listagem de chamados em suas categorias ------------------------------------------------------------

@login_required
def chamados_abertos(request):
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		novs_cham = obter_novos_chamados()
		Usuario = request.user
		chamados_ab = Chamado.objects.all().filter(status='aberto')
		context = {}

		context['chamados'] = chamados_ab
		context['Novos_Chamados'] = novs_cham
		context['Nome_Sistema'] = Nome_Sistema
		context['filtro'] = 'abertos'

		return render(request, "painel.html", context)

	else:

		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)
		
	


@login_required
def chamados_fechados(request):
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		novs_cham = obter_novos_chamados()
		Usuario = request.user
		chamados_ex = Chamado.objects.all().filter(status='fechado')
		context = {}

		context['chamados'] = chamados_ex
		context['Novos_Chamados'] = novs_cham
		context['Nome_Sistema'] = Nome_Sistema
		context['filtro'] = 'fechados'

		return render(request, "painel.html", context)

	else:
		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)
@login_required	
def chamados_excluidos(request):
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		novs_cham = obter_novos_chamados()
		Usuario = request.user
		chamados_ex = Chamado.objects.all().filter(status='excluido')
		context = {}

		context['chamados'] = chamados_ex
		context['Novos_Chamados'] = novs_cham
		context['Nome_Sistema'] = Nome_Sistema
		context['filtro'] = 'excluidos'

		return render(request, "painel.html", context)

	else:
		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)
		




@login_required
def chamados_resolvidos(request):
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		novs_cham = obter_novos_chamados()
		Usuario = request.user
		chamados_re = Chamado.objects.all().filter(status='resolvido')
		context = {}

		context['chamados'] = chamados_re
		context['Novos_Chamados'] = novs_cham
		context['Nome_Sistema'] = Nome_Sistema
		context['filtro'] = 'resolvidos'

		return render(request, "painel.html", context)
	else:
		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)
		
		

@login_required
def chamados_pendentes(request):
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		novs_cham = obter_novos_chamados()
		Usuario = request.user
		chamados_pe = Chamado.objects.all().filter(status='pendente')
		context['chamados'] = chamados_pe
		context['Novos_Chamados'] = novs_cham
		context['Nome_Sistema'] = Nome_Sistema
		context['filtro'] = 'pendentes'
		return render(request, "painel.html", context)
	else:

		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)
		
#-----------------FIM LISTAGEM DE CHAMADOS----------------------------------------------------------------------------------------------





@login_required
def painel(request):   #MOSTRA O PAINEL PRINCIPAL E TODOS OS CHAMADOS
	context = {}
	if request.user.is_atendente == True:  #CHECA SE O USUÁRIO É UM ATENDENTE, SE SIM, DÁ ACESSO AO PAINEL
		chamados_si = obter_chamados()
		novs_cham = obter_novos_chamados()
		Usuario = request.user

		
		
		context['Nome_Sistema'] = Nome_Sistema
		context['Novos_Chamados'] = novs_cham

		context['chamados'] = chamados_si
		context['filtro'] = 'todos'


		return render(request, "painel.html", context)
	else:
		messages.warning(request,'Você não tem acesso à essa página')
		return render(request, "home.html", context)


@login_required
@csrf_exempt
def alterar_status(request):
	if request.method =='POST' and request.is_ajax() == False:
		status_novo = request.POST.get('selecionar_status')
		id_chamado = request.POST.get('id_chamado')
		o_chamado = Chamado.objects.get(id=id_chamado)
		o_chamado.status = status_novo
		if status_novo == 'resolvido':
				o_chamado.foi_lido = true
				
		o_chamado.save()
		messages.success(request,'Status do chamado Nº {} defino como {} com sucesso!'.format(id_chamado,status_novo.upper()))
		return redirect('/chamado/{}'.format(id_chamado),request)


	if request.is_ajax() and request.method =='POST':
		lista_num_cham = []
		id_lido = request.POST.getlist('lista_ids[]')
		status = request.POST.get('status')
		for id_un in id_lido:
		
			Chamado_ler_un = Chamado.objects.get(id=id_un)
			Chamado_ler_un.status = status
			
			Chamado_ler_un.save()
			lista_num_cham.append(id_un)

		sort(lista_num_cham)
		
			

		messages.success(request,'chamados {} foi marcado como {}'.format(lista_num_cham,status))
			
		return HttpResponse('/painel/')
				
	


	else:
		print('não é ajax')
		return(HttpResponse,'haha')



@csrf_exempt
@login_required
def alterar_prioridade(request):
	if request.method =='POST' and request.is_ajax() == False:
		prioridade_nova = request.POST.get('selecionar_prioridade')
		id_chamado = request.POST.get('id_chamado')
		o_chamado = Chamado.objects.get(id=id_chamado)
		o_chamado.prioridade = prioridade_nova
		o_chamado.save()
		messages.success(request,'Prioridade do chamado Nº {} definida como {} com sucesso!'.format(id_chamado,prioridade_nova.upper()))
		return redirect('/chamado/{}'.format(id_chamado),request)


	if request.is_ajax() and request.method =='POST':
		lista_num_cham = []
		id_lido = request.POST.getlist('lista_ids[]')
		prioridade = request.POST.get('prioridade')
		for id_un in id_lido:
		
			Chamado_ler_un = Chamado.objects.get(id=id_un)
			Chamado_ler_un.prioridade = prioridade
			
			Chamado_ler_un.save()
			lista_num_cham.append(id_un)

		sort(lista_num_cham)
		
			#print('chamado {} lido foi marcado como {}'.format(id_un,prioridade))

		messages.success(request,'chamados {} foi marcado como {}'.format(lista_num_cham,prioridade))
			
		return HttpResponse('success')




# SEÇÃO DE USUARIOS
@login_required
def usuarios(request):
	context = {}
	usuarios = obter_usuarios()
	chamados_si = obter_chamados()
	novs_cham = obter_novos_chamados()
	Usuario = request.user


	chamados = Chamado.objects.all()

	

	
	numero_chamados = 0
	for usuario in usuarios:
		usuario.numero_chamados = Chamado.objects.filter(autor= usuario).count() 
				 # Representa a quantidade de chamados que cada usuário tem no sistema




	context['usuarios'] = usuarios
	context['Nome_Sistema'] = Nome_Sistema
	context['Novos_Chamados'] = novs_cham
	context['chamados'] = chamados



	return render(request, "usuarios.html", context)


@login_required
def ver_usuario(request,nome_usuario):
	context = {}
	usuario = Usuario.objects.get(username = nome_usuario)
	usuarios = obter_usuarios()
	chamados_si = obter_chamados()
	novs_cham = obter_novos_chamados()
	chamados = Chamado.objects.all()
	
	numero_chamados = 0
	for usuario in usuarios:
		usuario.numero_chamados = Chamado.objects.filter(autor= usuario).count() 
				 # Representa a quantidade de chamados que cada usuário tem no sistema

	context['usuario'] = usuario
	context['usuario'] = usuario

	
	context['Nome_Sistema'] = Nome_Sistema
	context['Novos_Chamados'] = novs_cham
	context['chamados'] = chamados



	return render(request, "usuario_un.html", context)	





def obter_usuarios():
	usuarios = Usuario.objects.all()
	return usuarios

def remover_usuario(nome_user):
	pass





# SEÇÃO DE ANEXOS

@csrf_exempt
@login_required
def upload_anexo(request):

	if request.method == 'POST':
		arquivos = request.FILES['input_arquivo']
		id_chamado = request.POST['id_chamado']

		nome_anexo = arquivos.name
		novo_anexo = Anexo.objects.create(titulo=nome_anexo,arquivo = arquivos)
		novo_anexo.save()
		chamado_obj = Chamado.objects.get(id=id_chamado)
		novo_cham_anexo = Anexos_chamado.objects.create(anexo = novo_anexo, chamado = chamado_obj )
		

		messages.success(request,'Anexo {} foi incluido com sucesso'.format(nome_anexo))
			
		return HttpResponseRedirect(f'/chamado/{id_chamado}')

@csrf_exempt
@login_required
def excluir_anexo(request):

	if request.method == 'POST':

		anexo_id = request.POST.get('anexo_id')
		dir_anterior = request.POST.get('dir_atual')
		nome_anexo = Anexo.objects.get(id=anexo_id).titulo

		Anexo.objects.get(id=anexo_id).delete()

		""" nome_anexo = arquivos.name
		novo_anexo = Anexo.objects.get(titulo=nome_anexo,arquivo = arquivos)
		novo_anexo.save()
		chamado_obj = Chamado.objects.get(id=anexo)
		novo_cham_anexo = Anexos_chamado.objects.create(anexo = novo_anexo, chamado = chamado_obj ) """
		

		messages.success(request,'Anexo {} foi excluído com sucesso'.format(nome_anexo))

		if dir_anterior != None:
			return redirect(dir_anterior)
		else:
			return redirect('home')

	



