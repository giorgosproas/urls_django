from django.db import models

# Create your models here.
class URLS(models.Model):
    url = models.CharField(max_length=500,unique=True)
    shortcode = models.CharField(max_length=6,unique=True)
    created = models.CharField(max_length=24)
    lastRedirect = models.CharField(max_length=24)
    redirectCount = models.IntegerField(default=0)

    
    def __str__(self):
        return self.url