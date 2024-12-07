from django.db import models
from django.urls import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to ='static/images/')
    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse_lazy('hero_list')