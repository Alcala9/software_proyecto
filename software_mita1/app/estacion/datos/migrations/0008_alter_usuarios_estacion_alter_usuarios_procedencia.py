# Generated by Django 5.0.2 on 2024-06-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0007_alter_usuarios_estacion_alter_usuarios_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='estacion',
            field=models.TextField(choices=[('1', 'Estacion meteorologica 1 Ojocaliente ')], max_length=1, verbose_name='Estacion'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='procedencia',
            field=models.TextField(choices=[('1', 'Universidad Autonoma de Zacatecas'), ('2', 'Sector privado'), ('3', 'Sector publico')], max_length=1, verbose_name='Procedencia'),
        ),
    ]