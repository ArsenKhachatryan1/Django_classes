# Generated by Django 4.1.7 on 2023-04-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_headerinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerinfo',
            name='account_en',
            field=models.CharField(max_length=50, null=True, verbose_name='accaunt'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='account_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='accaunt'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='cart_en',
            field=models.CharField(max_length=50, null=True, verbose_name='cart'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='cart_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='cart'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='checkout_en',
            field=models.CharField(max_length=50, null=True, verbose_name='checkout'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='checkout_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='checkout'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='country1_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country 1'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='country1_hy',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country 1'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='country2_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country 2'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='country2_hy',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country 2'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='login_en',
            field=models.CharField(max_length=50, null=True, verbose_name='login'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='login_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='login'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='logout_en',
            field=models.CharField(max_length=50, null=True, verbose_name='logout'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='logout_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='logout'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Site name'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='name_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='Site name'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='signup_en',
            field=models.CharField(max_length=50, null=True, verbose_name='signup'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='signup_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='signup'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='wishlist_en',
            field=models.CharField(max_length=50, null=True, verbose_name='wishlist'),
        ),
        migrations.AddField(
            model_name='headerinfo',
            name='wishlist_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='wishlist'),
        ),
    ]