# Generated by Django 2.0.2 on 2019-01-22 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0016_auto_20190121_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='turno',
            name='persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='turnos.Paciente'),
        ),
    ]