# Generated by Django 3.1.6 on 2021-02-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0002_auto_20210210_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageProduct',
            field=models.ImageField(upload_to='media/StoreApp/images'),
        ),
    ]
