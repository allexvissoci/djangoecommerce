# Generated by Django 2.1.2 on 2018-10-05 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
