# Generated by Django 4.1.5 on 2023-02-10 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb_guia', models.CharField(max_length=175)),
                ('apell_guia', models.CharField(max_length=175)),
                ('num_documento', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='sitio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sitio', models.CharField(max_length=150)),
                ('aforo', models.IntegerField(default=0)),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('hora_salida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb_visitante', models.CharField(max_length=175)),
                ('apell_visitante', models.CharField(max_length=175)),
                ('tipo_documento', models.CharField(max_length=20)),
                ('num_documento', models.CharField(max_length=11)),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=175)),
                ('apellidos', models.CharField(max_length=175)),
                ('correo', models.CharField(max_length=225)),
                ('contrasena', models.CharField(max_length=11)),
            ],
        ),
    ]
