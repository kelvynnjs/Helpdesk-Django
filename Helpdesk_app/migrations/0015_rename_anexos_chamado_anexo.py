# Generated by Django 3.2.4 on 2021-06-23 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0014_auto_20210623_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chamado',
            old_name='anexos',
            new_name='anexo',
        ),
    ]