# Generated by Django 3.2 on 2021-05-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0004_auto_20210501_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=30)),
                ('nome_completo', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=45)),
                ('place', models.CharField(max_length=45)),
            ],
        ),
    ]