from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Usuario
from django.urls import reverse
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def cadastro_usuario(request):

    if request.method == 'GET':
        return render(request, 'cadastro_usuarios.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        area_de_atuacao = request.POST.get('area_de_atuacao')
        tipo_usuario = request.POST.get('tipo_usuario')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user_obj = Usuario()

        user_obj.nome = nome
        user_obj.email = email
        user_obj.area_de_atuacao = area_de_atuacao
        user_obj.tipo_usuario = tipo_usuario
        user_obj.usuario = usuario
        user_obj.senha = senha

        user_obj.save()

        return HttpResponseRedirect(reverse('index') + '?success=true')
    
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        is_admin = bool(int(request.POST.get('is_admin')))
        
        try:
            if is_admin:
                user_obj = Usuario.objects.get(usuario=usuario, senha=senha, tipo_usuario="Administrador")
            else:
                user_obj = Usuario.objects.get(usuario=usuario, senha=senha)
        except Usuario.DoesNotExist:
            user_obj = None
        if user_obj is not None:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'error': 'Método de requisição não suportado.'}, status=405)

def tela_usuario(request):
    return render(request, 'tela_usuario.html')