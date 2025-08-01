# Generated by Django 5.2.4 on 2025-07-16 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Tipo de Veículo',
                'verbose_name_plural': 'Tipos de Veículos',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, unique=True, verbose_name='Placa')),
                ('brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vehicles', to='customers.customer', verbose_name='Proprietário')),
                ('vehicle_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vehicles', to='vehicles.vehicletype', verbose_name='Tipo de Veículos')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
    ]
