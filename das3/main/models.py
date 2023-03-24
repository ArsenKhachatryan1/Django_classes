from django.db import models

# Create your models here.


class Phone(models.Model):

    name = models.CharField('Phone name', max_length=60)
    img = models.ImageField('Phone image', upload_to='images')
    price = models.PositiveBigIntegerField('Phone price')
    date = models.DateTimeField('Phone date', auto_now=True)
    check_1 = models.BooleanField('Yes/No')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        ordering = ['-date']
    