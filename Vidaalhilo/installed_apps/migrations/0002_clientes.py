# Generated by Django 4.2.4 on 2023-10-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installed_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=8)),
            ],
        ),
    ]
