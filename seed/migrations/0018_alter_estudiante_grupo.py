# Generated by Django 3.2.8 on 2021-10-21 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0017_auto_20211021_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='seed.grupo'),
        ),
    ]
