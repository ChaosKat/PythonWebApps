from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Creator(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('creator_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def heroes(self):
        return Superhero.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Creator.objects.get_or_create(user=user)[0]


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