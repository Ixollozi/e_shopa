# Generated by Django 4.2.1 on 2023-06-14 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='product_image',
        ),
    ]
