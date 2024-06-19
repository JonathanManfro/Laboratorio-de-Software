from django import forms
from .models import Pesquisador

class PesquisadorForm(forms.ModelForm):
    class Meta:
        model = Pesquisador
        fields = ['area_de_atuacao', 'lattes', 'projetos', 'imagem_perfil']
