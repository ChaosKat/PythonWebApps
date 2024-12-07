from django.contrib import admin
from .models import Creator, Superhero, Article

admin.site.register(Creator)
admin.site.register(Superhero)
admin.site.register(Article)