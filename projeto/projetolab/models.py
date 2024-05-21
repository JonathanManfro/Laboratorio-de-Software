from django.db import models

class Pesquisa(models.Model):
    id = models.AutoField(primary_key=True)
    linha_de_busca = models.CharField(max_length=255)
    resultado = models.TextField()
    id_usuario = models.IntegerField()

    def buscar_informacoes(self):
        pass

class AreaDePesquisa(models.Model):
    id = models.AutoField(primary_key=True)
    nome_area = models.CharField(max_length=100)
    nome_subarea = models.CharField(max_length=100)

    def consulta_area(self):
        pass

class Producao(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    data_inicio = models.DateField()
    autores = models.ForeignKey('Pesquisador', on_delete=models.CASCADE)
    desenvolvimento = models.TextField()

    def exibir_producao(self):
        pass

    def cadastrar_producao(self):
        pass

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    area_de_atuacao = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def cadastrar_usuario(self):
        pass

class Fomento(models.Model):
    id = models.AutoField(primary_key=True)
    verba_aprovada = models.DecimalField(max_digits=10, decimal_places=2)

    def cadastro_de_acao_de_captacao(self):
        pass

    def exibir_acao(self):
        pass

class Fomentador(models.Model):
    cnpj = models.CharField(max_length=20)

class Pesquisador(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    area_de_atuacao = models.CharField(max_length=255)
    lattes = models.CharField(max_length=255)
    projetos = models.CharField(max_length=255)

    def exibir_pesquisador(self):
        pass

    def exibir_relacoes_entre_pesquisadores(self):
        pass