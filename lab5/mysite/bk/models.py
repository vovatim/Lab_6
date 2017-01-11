from django.db import models

class TovarModel(models.Model):
    name = models.CharField(max_length=70)
    desc = models.CharField(max_length=300)
    cout = models.IntegerField()