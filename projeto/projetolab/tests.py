from django.test import TestCase
from projetolab.models import Usuario, Pesquisador, CaptacaoRecurso, Producao
from datetime import date
import os
from django.conf import settings

class CadastroPesquisadorTest(TestCase):
    def test_cadastro_pesquisador_e_usuario(self):
        usuario = Usuario.objects.create(
            nome="João Silva",
            email="joaosilva@example.com",
            area_de_atuacao="Ciências da Computação",
            tipo_usuario="Pesquisador",
            usuario="joaosilva",
            senha="senha123"
        )

        pesquisador = Pesquisador.objects.create(
            area_de_atuacao="Ciências da Computação",
            lattes="http://lattes.cnpq.br/123456789",
            projetos="Projeto de Pesquisa 1",
            usuario_fk=usuario,
            imagem_perfil=None
        )

        self.assertEqual(pesquisador.usuario_fk, usuario)
        self.assertEqual(pesquisador.area_de_atuacao, "Ciências da Computação")

class ConexaoBancoDadosTest(TestCase):
    def test_conexao_banco(self):
        db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        self.assertTrue(os.path.exists(db_path), "O arquivo do banco de dados não existe.")

class CadastroCaptacaoRecursoTest(TestCase):
    def test_cadastro_captacao_recurso(self):
        usuario = Usuario.objects.create(
            nome="Maria Fernanda",
            email="mariafernanda@example.com",
            area_de_atuacao="Bioquímica",
            tipo_usuario="Pesquisador",
            usuario="mariafernanda",
            senha="senhasupersegura"
        )

        pesquisador = Pesquisador.objects.create(
            area_de_atuacao="Bioquímica",
            lattes="http://lattes.cnpq.br/987654321",
            projetos="Projeto de Pesquisa Bioquímica",
            usuario_fk=usuario,
            imagem_perfil=None
        )

        producao = Producao.objects.create(
            tipo="teste",
            data_inicio=date(2023, 7, 1),
            desenvolvimento="desenvolvimento teste"
        )

        captacao_recurso = CaptacaoRecurso.objects.create(
            pesquisador=pesquisador,
            producao=producao,
            valor=50000.00
        )

        self.assertEqual(captacao_recurso.valor, 50000.00)
        self.assertEqual(captacao_recurso.pesquisador, pesquisador)
        self.assertEqual(captacao_recurso.producao, producao)
