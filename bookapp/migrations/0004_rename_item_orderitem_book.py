# Generated by Django 3.2.11 on 2024-01-11 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_item_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='book',
        ),
    ]