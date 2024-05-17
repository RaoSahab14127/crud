from django.db import models

class Cars(models.Model):
    modelname = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    year = models.IntegerField()
    engine = models.CharField(max_length=100)
    def __str__(self):
        return self.modelname

