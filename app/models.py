from django.db import models
import datetime

class DcHero(models.Model):
    pageId =           models.PositiveIntegerField(null=False, blank=False,primary_key=True)	
    name = 	           models.CharField(max_length=200,null=True, blank=True)
    urlslug =          models.CharField(max_length=200,null=True, blank=True)
    identity =		   models.CharField(max_length=200,null=True, blank=True)
    align =		       models.CharField(max_length=200,null=True, blank=True)
    eye =		       models.CharField(max_length=200,null=True, blank=True)
    hair =		       models.CharField(max_length=200,null=True, blank=True)
    sex =		       models.CharField(max_length=200,null=True, blank=True)
    gsm =	           models.CharField(max_length=200,null=True, blank=True)
    alive =		       models.CharField(max_length=200,null=True, blank=True)
    appearances =      models.PositiveIntegerField(null=True, blank=True)	
    firstAppearance = models.CharField(max_length=200,null=True, blank=True)
    year =		       models.PositiveIntegerField(null=True, blank=True)	


    def __str__(self):
        return f"The DC hero: {self.name} was created at: {self.year} and appears first time on: {self.firstAppearance}"