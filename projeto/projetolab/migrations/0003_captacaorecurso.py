# Generated by Django 4.2.13 on 2024-06-29 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetolab', '0002_pesquisador_imagem_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaptacaoRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pesquisador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetolab.pesquisador')),
                ('producao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetolab.producao')),
            ],
        ),
    ]