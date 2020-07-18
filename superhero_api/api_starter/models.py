from django.db import models

class Superhero(models.Model):
    hero_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    universe = models.CharField(max_length=100)

    def __str__(self):
        return self.name
