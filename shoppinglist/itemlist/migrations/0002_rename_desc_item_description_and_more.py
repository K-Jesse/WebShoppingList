# Generated by Django 4.0.4 on 2022-05-31 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ammount',
            new_name='quantity',
        ),
    ]
