# Generated by Django 3.1.7 on 2021-04-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_ventas_por_enviar_sesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas_por_enviar',
            name='autorizacion',
            field=models.CharField(default=12, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas_por_enviar',
            name='verificacion',
            field=models.CharField(default=12, max_length=10000),
            preserve_default=False,
        ),
    ]
