from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Usuario, Projeto, Pesquisador, Producao, AreaDePesquisa
from django.urls import reverse
from django.http import JsonResponse
import json

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
        lattes = request.POST.get('lattes')
        projetos = request.POST.get('projetos')

        user_obj = Usuario()

        user_obj.nome = nome
        user_obj.email = email
        user_obj.area_de_atuacao = area_de_atuacao
        user_obj.tipo_usuario = tipo_usuario
        user_obj.usuario = usuario
        user_obj.senha = senha

        user_obj.save()

        if tipo_usuario == 'Pesquisador':
            pesquisador_obj = Pesquisador()

            pesquisador_obj.area_de_atuacao = area_de_atuacao
            pesquisador_obj.lattes = lattes
            pesquisador_obj.projetos = projetos
            pesquisador_obj.usuario_fk = user_obj

            pesquisador_obj.save()

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

def cadastrar_projetos(request):
    if request.method == 'GET':
        return render(request, 'cadastro_projetos.html')
    
    elif request.method == 'POST':

        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        participantes = request.POST.get('participantes') 
        objetivos = request.POST.get('objetivos') 
        resultados = request.POST.get('resultados')  

        projeto_obj = Projeto()

        projeto_obj.titulo = titulo
        projeto_obj.descricao = descricao
        projeto_obj.participantes = participantes
        projeto_obj.objetivos = objetivos
        projeto_obj.resultados = resultados

        projeto_obj.save()

        return render(request, 'sucesso.html')
        
def visualizar_pesquisadores(request):
    pesquisadores = Pesquisador.objects.all()
    
    areas_de_atuacao = Pesquisador.objects.values_list('area_de_atuacao', flat=True)
    
    areas_de_atuacao_unicas = set(areas_de_atuacao)
    
    return render(request, 'visualizar_pesquisadores.html', {'pesquisadores': pesquisadores, 'areas_de_atuacao_unicas': areas_de_atuacao_unicas})

def cadastrar_producao(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        data_inicio = request.POST.get('data_inicio')
        desenvolvimento = request.POST.get('desenvolvimento')
        autores_ids = request.POST.getlist('autores')

        producao = Producao.objects.create(
            tipo=tipo,
            data_inicio=data_inicio,
            desenvolvimento=desenvolvimento
        )

        producao.autores.set(autores_ids)

        return render(request, 'sucesso.html')

    pesquisadores = Pesquisador.objects.all()
    return render(request, 'cadastro_producao.html', {'pesquisadores': pesquisadores})

def visualizar_producoes(request):
    pesquisador_id = request.POST.get('pesquisador_id')
    pesquisador = Pesquisador.objects.get(id=pesquisador_id)
    
    producoes_do_pesquisador = Producao.objects.filter(autores=pesquisador)
    
    detalhes_das_producoes = producoes_do_pesquisador.values()

    return render(request, 'visualizar_producoes.html', {'detalhes_das_producoes': detalhes_das_producoes})

def visualizar_areas_de_pesquisa(request):
    areas_de_pesquisa = AreaDePesquisa.objects.all()
    nomes_areas_unicas = AreaDePesquisa.objects.values_list('nome_area', flat=True).distinct()
    return render(request, 'visualizar_areas_de_pesquisa.html', {'areas_de_pesquisa': areas_de_pesquisa, 'nomes_areas_unicas': nomes_areas_unicas})

def visualizar_relacoes_entre_pesquisadores(request):
    pesquisadores = Pesquisador.objects.all()

    conexoes = {}

    for pesquisador in pesquisadores:
        producoes_pesquisador = Producao.objects.filter(autores=pesquisador)

        for outra_pessoa in pesquisadores:
            if pesquisador != outra_pessoa:
                producoes_outra_pessoa = Producao.objects.filter(autores=outra_pessoa)

                producoes_em_comum = producoes_pesquisador.intersection(producoes_outra_pessoa)

                if producoes_em_comum.exists():
                    nome_pesquisador = pesquisador.usuario_fk.nome
                    nome_outra_pessoa = outra_pessoa.usuario_fk.nome

                    if nome_pesquisador not in conexoes:
                        conexoes[nome_pesquisador] = {}

                    conexoes[nome_pesquisador][nome_outra_pessoa] = producoes_em_comum.count()

    conexoes_json = json.dumps(conexoes)

    return render(request, 'visualizar_relacoes_entre_pesquisadores.html', {'conexoes_json': conexoes_json})