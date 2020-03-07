from django.db import models

# Create your models here.


class Mac(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    mac = models.CharField(verbose_name='MAC地址', max_length=255)
