# Generated by Django 4.0.1 on 2022-01-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilinos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquilinos',
            name='unidade_inquilino',
        ),
        migrations.AlterField(
            model_name='unidades',
            name='proprietario_unidade',
            field=models.CharField(max_length=200),
        ),
    ]
