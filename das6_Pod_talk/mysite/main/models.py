from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    badge_1 = models.CharField('badge_1', max_length=20, blank=True)
    badge_2 = models.CharField('badge_2', max_length=20, blank=True)
    kayq_1 = models.CharField('kayq_', max_length=20, blank=True)
    kayq_1_link = models.CharField('kayq_1_link', max_length=50, blank=True)
    kayq_2 = models.CharField('kayq_2', max_length=20, blank=True)
    kayq_2_link = models.CharField('kayq_2_link', max_length=50, blank=True)
    kayq_3 = models.CharField('kayq_3', max_length=20, blank=True)
    kayq_3_link = models.CharField('kayq_3_link', max_length=50, blank=True)
    verification = models.BooleanField('Yes/No', null=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'


class Topic(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    info = models.CharField('Info', max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class Download(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    link = models.CharField('link', max_length=60,)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'


class Social(models.Model):
    name = models.CharField('Name', max_length=50)
    link = models.CharField('link', max_length=60,)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'



class Contact(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    company = models.CharField('User name', max_length=50)
    message = models.TextField('User message')

    def __str__(self) -> str:
        return self.name