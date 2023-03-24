from django.db import models

# Create your models here.


class Sitename(models.Model):
    sitename = models.CharField('Site name', max_length=50)


class Portfolio(models.Model):
    name = models.CharField('Name', max_length=50)
    price = models.CharField('Price', max_length=50)
    img = models.ImageField('Small image', upload_to='images')
    img_big = models.ImageField('Big image', upload_to='images')

    def __str__(self) -> str:
        return self.name
    

class Story(models.Model):
    name = models.CharField('Name', max_length=20)
    text = models.TextField('Text')
    img = models.ImageField('Story image', upload_to='images')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
    
   
    
class Contact(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    message = models.TextField('User message')

    def __str__(self) -> str:
        return self.name