#PROGRAMA SIMPLES PARA GERAÇÃO DE DIAGRAMA DE HERANÇA DE TEMPLATES - KELVYNN JOSÉ DA SILVA 
import re
import os

#diretorio_analise = r"C:\Users\kelvy\Desktop\Helpdesk-Django\Helpdesk_app\templates"

diretorio_analise = r"C:\Users\kelvy\Desktop\Helpdesk-Django\UML\TESTE"



#https://regex101.com/

#EXEMPLO DE REGEX PARA ENCONTRAR "{% INCLUDE 'nome_arquivo.html'%}" com uma ou duas aspas :    /{% include "\w+.html" %}|{% include '\w+.html'%}/gm

#exemplo com extends   {% include "\w+.html" %}|{% include '\w+.html'%}|{% extends '\w+.html' %}


regex_template = re.compile(r'')



with os.scandir(diretorio_analise) as dirs:
    for entry in dirs:
        if entry.is_file() == True:
            file = open(entry.name, 'r')


def verificar_arquivo(texto):
    lista_achados = []








