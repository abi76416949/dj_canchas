# Generated by Django 5.2 on 2025-04-27 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courts', '0001_initial'),
        ('polideportivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courtmodel',
            name='polideportivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courts', to='polideportivos.polideportivomodel'),
        ),
    ]
