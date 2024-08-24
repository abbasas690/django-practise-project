from django.db import models

# Create your models here.

class PageVisit(models.Model):
    page=models.TextField(null=True,blank=True)
    timeStamp=models.DateTimeField(auto_now=True)
    