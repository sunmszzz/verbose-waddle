from django.db import models

# Create your models here.


class Mac(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    mac = models.CharField(verbose_name='MAC地址', max_length=255)

class Homework (models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    number = models.CharField(verbose_name='学号', max_length=32)
    is_upload = models.CharField(verbose_name='是否上传', max_length=32, null=True)
    upload_time = models.CharField(verbose_name='上传时间', max_length=64, null=True)