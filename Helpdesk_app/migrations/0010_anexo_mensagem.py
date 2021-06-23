# Generated by Django 3.2.4 on 2021-06-22 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0009_alter_chamado_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=150)),
                ('arquivo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_mensagem', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('autor_mensagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_mensagem', to=settings.AUTH_USER_MODEL)),
                ('receptor_mensagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor_mensagem', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]