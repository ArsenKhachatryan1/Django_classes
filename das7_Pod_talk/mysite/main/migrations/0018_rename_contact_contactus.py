# Generated by Django 4.1.7 on 2023-03-29 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_aboutpod_alter_ourstory_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactUs',
        ),
    ]