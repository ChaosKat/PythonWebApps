from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView
from django.urls import reverse_lazy

from .models import Superhero

class HeroView(RedirectView):
    url = reverse_lazy('hero_list')

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'

class HeroCreateView(CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')