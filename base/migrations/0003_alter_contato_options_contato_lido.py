# Generated by Django 4.2.5 on 2023-10-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reservadebanho'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-nome'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulário de Contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
