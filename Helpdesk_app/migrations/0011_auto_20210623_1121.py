# Generated by Django 3.2.4 on 2021-06-23 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk_app', '0010_anexo_mensagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anexo',
            name='local',
        ),
        migrations.AddField(
            model_name='mensagem',
            name='anexo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Helpdesk_app.anexo'),
        ),
        migrations.AlterField(
            model_name='anexo',
            name='arquivo',
            field=models.ImageField(upload_to='anexos/'),
        ),
    ]