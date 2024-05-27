from django.db import models

# class Cars(models.Model):
#     modelname = models.CharField(max_length=200)
#     colour = models.CharField(max_length=200)
#     year = models.IntegerField()
#     engine = models.CharField(max_length=100)
#     def __str__(self):
#         return self.modelname


# Create your models here.
class Actors(models.Model):
    fullname =  models.CharField(max_length=200, unique= True)
    dob = models.DateField()
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

class Movies(models.Model):
    imdb_rating = models.FloatField()
    views = models.IntegerField()
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    title = models.CharField
    synopsis = models.CharField(max_length=200)
    def __str__(self):
        return self.title