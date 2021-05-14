from django import forms



class UsuarioForm(forms.Form):
    nome_usuario = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome de usuário'}))  #nome do usuário
    nome_completo = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome completo'})) # nome completo do usuário
    senha_usuario = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'})) #senha do usuario
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail'})) #email do usuário
    data_criacao = forms.DateTimeField(auto_now_add=True, editable=False, blank=False) #data de criação do usuário

