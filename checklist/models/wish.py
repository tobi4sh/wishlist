from django.db import models
from django.conf import settings

class Wish(models.Model):

    fullfilled = models.BooleanField(default=False)
    item = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    fullfiller = settings.AUTH_USER_MODEL
