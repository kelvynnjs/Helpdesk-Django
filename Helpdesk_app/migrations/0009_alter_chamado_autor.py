# Generated by Django 3.2.4 on 2021-06-21 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0008_rename_is_lido_chamado_foi_lido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
