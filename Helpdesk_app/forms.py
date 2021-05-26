from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import fields



#place = models.CharField(verbose_name="Lugar(setor,departamento ou seção)",max_length=45) #departam   ento/local onde o usuário solicitante se encontra (onde o suporte acontece)

class CadastrarUsuario(UserCreationForm):
    nome_completo = forms.CharField(label="Nome completo",max_length=60) # nome completo do usuário
    email = forms.EmailField(label="E-mail") #email do usuário
    #data_criacao = forms.DateTimeField(label="Data de criação do usuário",auto_now_add=True, editable=True, blank=False) #data de criação do usuário
    


    class Meta:
        model = User
        fields = ['username','nome_completo','email','password1','password2']
        






  # nome_usuario = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome de usuário'}))  #nome do usuário
   # nome_completo = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome completo'})) # nome completo do usuário
    #senha_usuario = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'})) #senha do usuario
    #email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail'})) #email do usuário


