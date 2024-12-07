# Generated by Django 5.1.3 on 2024-12-07 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias_Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('reservacion_fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platillo', models.CharField(max_length=255, unique=True)),
                ('categoria_Comida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categorias_comidas')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Sugerencias_Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugerencia', models.CharField(max_length=255)),
                ('categoria_comida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categorias_comidas')),
            ],
        ),
    ]
