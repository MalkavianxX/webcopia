# Generated by Django 3.1.7 on 2021-03-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('contenido', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='')),
                ('creted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'articulo',
                'verbose_name_plural': 'articulos',
            },
        ),
    ]
