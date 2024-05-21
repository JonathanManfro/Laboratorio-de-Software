from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_usuario/', views.cadastro_usuario, name='cadastrar_usuario'),
    path('login/', views.login_view, name='login_usuario'),
    path('tela_usuario/', views.tela_usuario, name='tela_usuario'),
    path('cadastrar_projeto/', views.cadastrar_projetos, name='cadastrar_projeto')
]
