# Generated by Django 4.2.4 on 2023-10-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installed_apps', '0003_alter_clientes_direccion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articulos',
            new_name='Articulo',
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
    ]