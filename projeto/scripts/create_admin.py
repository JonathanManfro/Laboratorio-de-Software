import os
import django

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from projetolab.models import Usuario

def create_admin_user():
    if not Usuario.objects.filter(usuario='admin').exists():
        admin = Usuario.objects.create(
            nome='Admin',
            email='admin@admin.com',
            area_de_atuacao='Administração',
            tipo_usuario='Administrador',
            usuario='admin',
            senha='admin'
        )
        print('Usuário administrador criado com sucesso!')
    else:
        print('Usuário administrador já existe no banco de dados.')

if __name__ == "__main__":
    create_admin_user()
