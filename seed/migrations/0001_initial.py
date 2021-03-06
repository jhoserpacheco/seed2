# Generated by Django 3.2.8 on 2021-12-20 22:10

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('url_img', models.CharField(blank=True, default='', max_length=250)),
                ('is_estudiante', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_docente', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EstructuraDeDatos',
            fields=[
                ('codigo_ed', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_ed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('codigo_grupo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('estudiantes', models.FileField(blank=True, null=True, upload_to='estudiantes/')),
                ('estado', models.CharField(choices=[('AC', 'ACTIVO'), ('IN', 'INACTIVO'), ('AR', 'ARCHIVADO')], default='AC', max_length=9)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='seed.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='seed.usuario')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('codigo_tema', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('nombre_tema', models.CharField(default='', max_length=50)),
                ('grupo_tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.grupo')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
                'ordering': ['nombre_tema'],
            },
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_ac', models.CharField(max_length=50, verbose_name='Nombre de la actividad')),
                ('descripcion', models.TextField(max_length=350)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('es_visible', models.BooleanField(default=True)),
                ('estructura_de_datos', models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='seed.estructuradedatos')),
                ('tema_actividad', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seed.tema')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['nombre_ac'],
            },
        ),
        migrations.AddField(
            model_name='grupo',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.docente'),
        ),
        migrations.CreateModel(
            name='Estudiante_Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE'), ('C', 'CALIFICADA')], default='P', max_length=2)),
                ('nota', models.FloatField(default=0.0)),
                ('comentario', models.TextField(default='No hay comentarios.', max_length=500)),
                ('fecha_entrega', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('entregaFile', models.FileField(blank=True, null=True, upload_to='entregas/')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.actividad')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.estudiante')),
            ],
            options={
                'verbose_name': 'Estudiante_Actividad',
                'verbose_name_plural': 'Estudiantes_Actividades',
                'ordering': ['estado'],
            },
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.grupo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='estudianteAct',
            field=models.ManyToManyField(through='seed.Estudiante_Actividad', to='seed.Estudiante'),
        ),
    ]
