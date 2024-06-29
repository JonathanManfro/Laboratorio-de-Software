from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_usuario/', views.cadastro_usuario, name='cadastrar_usuario'),
    path('login/', views.login_view, name='login_usuario'),
    path('tela_usuario/', views.tela_usuario, name='tela_usuario'),
    path('cadastrar_projeto/', views.cadastrar_projetos, name='cadastrar_projeto'),
    path('visualizar_pesquisadores/', views.visualizar_pesquisadores, name='visualizar_pesquisadores'),
    path('cadastrar_producao/', views.cadastrar_producao, name='cadastrar_producao'),
    path('visualizar_producoes/', views.visualizar_producoes, name='visualizar_producoes'),
    path('visualizar_areas_de_pesquisa/', views.visualizar_areas_de_pesquisa, name='visualizar_areas_de_pesquisa'),
    path('visualizar_relacoes_entre_pesquisadores/', views.visualizar_relacoes_entre_pesquisadores, name='visualizar_relacoes_entre_pesquisadores'),
    path('visualizar_perfil/', views.visualizar_perfil, name='visualizar_perfil'),
    path('criar-captacao-recurso/', views.criar_captacao_recurso, name='criar_captacao_recurso'),
    path('visualizar-captacoes-recurso/', views.visualizar_captacoes_recurso, name='visualizar_captacoes_recurso'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

