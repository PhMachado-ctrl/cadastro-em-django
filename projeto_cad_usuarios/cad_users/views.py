from django.shortcuts import render
from .models import Usuario #Importa os models da classe

def home(request):
    #Retorna o Arquivo home.html
    return render(request,'usuarios/home.html')

def usuarios(request):
    '''Salvar os dados da tela para o banco de dados.'''
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save() #Salva as informações
    '''Exibir todos os usuários já cadastrados emuma nova página'''
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    '''Retornar os dados para página de listagem de usuarios'''
    return render(request,'usuarios/usuarios.html', usuarios)