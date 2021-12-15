# Generated by Django 3.2.8 on 2021-11-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0004_estudiante_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='estado',
            field=models.CharField(choices=[('AC', 'ACTIVO'), ('IN', 'INACTIVO'), ('AR', 'ARCHIVADO')], default='AC', max_length=9),
        ),
    ]
