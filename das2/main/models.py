from django.db import models

# Create your models here.


class Contact(models.Model):

    user_name = models.CharField('User name', max_length=50)
    user_email = models.EmailField('User email')
    user_phone = models.CharField('User phone', max_length=50)
    user_review = models.TextField('User review')

    def __str__(self) -> str:
        return self.user_name