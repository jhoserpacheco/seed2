# Generated by Django 3.2.8 on 2021-10-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0003_auto_20211021_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='codigo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='codigo_grupo',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
