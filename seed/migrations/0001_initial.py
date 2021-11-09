# Generated by Django 3.2.8 on 2021-11-03 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_ac', models.CharField(max_length=50, verbose_name='Nombre de la actividad')),
                ('descripcion', models.TextField(max_length=350)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('es_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['nombre_ac'],
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(blank=True, default='', max_length=50)),
                ('url_img', models.CharField(blank=True, default='', max_length=250)),
                ('es_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='EstructuraDeDatos',
            fields=[
                ('codigo_ed', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_ed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('url_img', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('codigo_grupo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('estado', models.CharField(choices=[('AC', 'ACTIVO'), ('IN', 'INACTIVO'), ('AR', 'ARCHIVADO')], default='AC', max_length=2)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.docente')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('codigo_tema', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('nombre_tema', models.CharField(default='', max_length=50)),
                ('grupo_tema', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seed.grupo')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
                'ordering': ['nombre_tema'],
            },
        ),
        migrations.CreateModel(
            name='Estudiate_Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE'), ('C', 'CALIFICADA')], default='P', max_length=2)),
                ('nota', models.FloatField(default=0.0)),
                ('comentario', models.TextField(default='No hay comentarios.', max_length=500)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.actividad')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.estudiante')),
            ],
            options={
                'verbose_name': 'Estudiante_Actividad',
                'verbose_name_plural': 'Estudiantes_Actividades',
                'ordering': ['estado'],
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='estructura_de_datos',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='seed.estructuradedatos'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='estudiante_actividad',
            field=models.ManyToManyField(through='seed.Estudiate_Actividad', to='seed.Estudiante'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='tema_actividad',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seed.tema'),
        ),
    ]
