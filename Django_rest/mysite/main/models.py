from django.db import models

# Create your models here.


class Phone(models.Model):

    name = models.CharField('Phone name', max_length=60)
    price = models.PositiveBigIntegerField('Phone price')
    img = models.ImageField('Phone image', upload_to='images', null=True)

    def __str__(self) -> str:
        return self.name
    

class Nout(models.Model):

    name = models.CharField('Nout name', max_length=60)
    price = models.PositiveBigIntegerField('Nout price')

    def __str__(self) -> str:
        return self.name