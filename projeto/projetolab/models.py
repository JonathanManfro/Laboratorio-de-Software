from django.db import models

class Pesquisa(models.Model):
    id = models.AutoField(primary_key=True)
    linha_de_busca = models.CharField(max_length=255)
    resultado = models.TextField()
    id_usuario = models.IntegerField()

class AreaDePesquisa(models.Model):
    id = models.AutoField(primary_key=True)
    nome_area = models.CharField(max_length=100)
    nome_subarea = models.CharField(max_length=100)

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    participantes = models.CharField(max_length=255)
    objetivos = models.CharField(max_length=255)
    resultados = models.CharField(max_length=255)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    area_de_atuacao = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Fomento(models.Model):
    id = models.AutoField(primary_key=True)
    verba_aprovada = models.DecimalField(max_digits=10, decimal_places=2)

class Fomentador(models.Model):
    cnpj = models.CharField(max_length=20)

class Pesquisador(models.Model):
    id = models.AutoField(primary_key=True)
    area_de_atuacao = models.CharField(max_length=255)
    lattes = models.CharField(max_length=255)
    projetos = models.CharField(max_length=255)
    usuario_fk = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Producao(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    data_inicio = models.DateField()
    autores = models.ManyToManyField(Pesquisador)
    desenvolvimento = models.TextField()