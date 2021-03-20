from django.db import models

# Create your models here.
class crud(models.Model):
    title=models.CharField(max_length=70)
    key=models.CharField(max_length=20)
    desc=models.CharField(max_length=1000)

