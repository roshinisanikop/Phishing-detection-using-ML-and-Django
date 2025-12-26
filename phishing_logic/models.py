from django.db import models

# Create your models here.


class phishing(models.Model):
    URLphish = models.URLField(max_length=200)
