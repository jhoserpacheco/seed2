# Generated by Django 3.2.7 on 2021-10-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0024_auto_20211026_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='url_img',
            field=models.CharField(default='', max_length=250),
        ),
    ]
