import os
import django
from projetolab.models import Usuario, AreaDePesquisa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

def create_admin_user():
    if not Usuario.objects.filter(usuario='admin').exists():
        Usuario.objects.create(
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

def populate_area_de_pesquisa():
    areas_de_pesquisa = [
        ('Matemática', 'Ciências Exatas e da Terra'),
        ('Astronomia', 'Ciências Exatas e da Terra'),
        ('Física', 'Ciências Exatas e da Terra'),
        ('Química', 'Ciências Exatas e da Terra'),
        ('Geografia Física', 'Ciências Exatas e da Terra'),
        ('Biologia Geral', 'Ciências Biológicas'),
        ('Bioquímica', 'Ciências Biológicas'),
        ('Fisiologia', 'Ciências Biológicas'),
        ('Biofísica', 'Ciências Biológicas'),
        ('Farmacologia', 'Ciências Biológicas'),
        ('Imunologia', 'Ciências Biológicas'),
        ('Microbiologia', 'Ciências Biológicas'),
        ('Parasitologia', 'Ciências Biológicas'),
        ('Botânica', 'Ciências Biológicas'),
        ('Zoologia', 'Ciências Biológicas'),
        ('Engenharia Civil', 'Engenharias'),
        ('Engenharia Elétrica', 'Engenharias'),
        ('Engenharia Mecânica', 'Engenharias'),
        ('Engenharia Química', 'Engenharias'),
        ('Engenharia de Materiais e Metalúrgica', 'Engenharias'),
        ('Engenharia de Produção', 'Engenharias'),
        ('Engenharia Sanitária', 'Engenharias'),
        ('Engenharia de Minas', 'Engenharias'),
        ('Engenharia de Transportes', 'Engenharias'),
        ('Medicina', 'Ciências da Saúde'),
        ('Odontologia', 'Ciências da Saúde'),
        ('Farmácia', 'Ciências da Saúde'),
        ('Enfermagem', 'Ciências da Saúde'),
        ('Saúde Coletiva', 'Ciências da Saúde'),
        ('Nutrição', 'Ciências da Saúde'),
        ('Agronomia', 'Ciências Agrárias'),
        ('Recursos Florestais e Engenharia Florestal', 'Ciências Agrárias'),
        ('Engenharia Agrícola', 'Ciências Agrárias'),
        ('Zootecnia', 'Ciências Agrárias'),
        ('Recursos Pesqueiros e Engenharia de Pesca', 'Ciências Agrárias'),
        ('Administração', 'Ciências Sociais Aplicadas'),
        ('Economia', 'Ciências Sociais Aplicadas'),
        ('Direito', 'Ciências Sociais Aplicadas'),
        ('Arquitetura e Urbanismo', 'Ciências Sociais Aplicadas'),
        ('Comunicação', 'Ciências Sociais Aplicadas'),
        ('Museologia', 'Ciências Sociais Aplicadas'),
        ('Serviço Social', 'Ciências Sociais Aplicadas'),
        ('Planejamento Urbano e Regional', 'Ciências Sociais Aplicadas'),
        ('Desenvolvimento Rural', 'Ciências Sociais Aplicadas'),
        ('Filosofia', 'Ciências Humanas'),
        ('Sociologia', 'Ciências Humanas'),
        ('Antropologia', 'Ciências Humanas'),
        ('História', 'Ciências Humanas'),
        ('Geografia', 'Ciências Humanas'),
        ('Psicologia', 'Ciências Humanas'),
        ('Educação', 'Ciências Humanas'),
        ('Linguística', 'Linguística, Letras e Artes'),
        ('Letras', 'Linguística, Letras e Artes'),
        ('Artes', 'Linguística, Letras e Artes')
    ]

    for nome_subarea, nome_area in areas_de_pesquisa:
        AreaDePesquisa.objects.get_or_create(nome_subarea=nome_subarea, nome_area=nome_area)

    print('Áreas de pesquisa populadas com sucesso!')
