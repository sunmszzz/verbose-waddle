# Generated by Django 2.1.8 on 2020-03-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='upload_time',
            field=models.CharField(max_length=64, null=True, verbose_name='上传时间'),
        ),
    ]