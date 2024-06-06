from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Zikr(models.Model):
    zikr = models.CharField(max_length=3000, null=True, blank=True)
    zikr_arabic = models.CharField(max_length=3000, null=True, blank=True)
    zikr_mean = models.CharField(max_length=3000, null=True, blank=True)
    send = models.BooleanField(default=False) 
 
    def __str__(self):
        return self.zikr
