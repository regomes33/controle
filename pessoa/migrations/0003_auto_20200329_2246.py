# Generated by Django 3.0.4 on 2020-03-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20200324_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=13, unique=True, verbose_name='CPF'),
        ),
    ]
