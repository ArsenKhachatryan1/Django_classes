# Generated by Django 4.1.7 on 2023-03-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_phone_options_phone_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['-date'], 'verbose_name': 'Phone', 'verbose_name_plural': 'Phones'},
        ),
        migrations.AddField(
            model_name='phone',
            name='check_1',
            field=models.BooleanField(default=1, verbose_name='Yes/No'),
            preserve_default=False,
        ),
    ]
