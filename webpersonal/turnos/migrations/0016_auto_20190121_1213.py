# Generated by Django 2.0.2 on 2019-01-21 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0015_paciente_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['nombre', 'apellido'], 'verbose_name': 'paciente', 'verbose_name_plural': 'pacientes'},
        ),
    ]
