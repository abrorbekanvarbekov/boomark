from django.db import models
from django.urls import reverse
# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=30)
    url = models.URLField('Site Url')
    

    def __str__(self):
        return "name: "+self.site_name+",  url: "+self.url

    def get_absolute_url(self):
        return reverse('detail',args=[self.id])