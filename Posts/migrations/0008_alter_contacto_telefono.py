# Generated by Django 4.1.3 on 2022-11-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_contacto_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
