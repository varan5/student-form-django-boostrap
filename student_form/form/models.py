from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name