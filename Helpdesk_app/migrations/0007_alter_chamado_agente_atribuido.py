# Generated by Django 3.2 on 2021-06-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0006_alter_chamado_prioridade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='agente_atribuido',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
