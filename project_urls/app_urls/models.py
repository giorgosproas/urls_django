from django.db import models

# Create your models here.
class URLS(models.Model):
    url = models.URLField(max_length=500)
    shortcode = models.CharField(max_length=6,unique=True)
    created = models.CharField(max_length=24)
    lastRedirect = models.CharField(max_length=24)
    redirectCount = models.IntegerField(default=0)

    
    def __str__(self):
        return self.url