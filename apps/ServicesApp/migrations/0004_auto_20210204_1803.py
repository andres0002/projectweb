# Generated by Django 3.1.6 on 2021-02-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicesApp', '0003_auto_20210204_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='imageService',
            field=models.ImageField(upload_to='media/ServicesApp/images'),
        ),
    ]
