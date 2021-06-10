from django.db import models

# Create your models here.

class Service(models.Model):
    titleService = models.CharField(max_length=60)
    contentService = models.CharField(max_length=60)
    imageService = models.ImageField(upload_to='media/ServicesApp/images')
    createDateService = models.DateTimeField(auto_now_add=True)
    updateDateService = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.titleService