from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Superhero, Creator

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


def list_articles(creator):
    return dict(heroes=Superhero.objects.filter(creator=creator))

def get_creator(user):
    return Creator.objects.get_or_create(user=user)[0]

class CreatorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/hero/'
        return f'/creator/{get_creator(self.request.user).pk}'

class CreatorDetailView(DetailView):
    model = Creator
    template_name = 'creator/detail.html'
    context_object_name = 'creator'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_articles(kwargs.get('object')))
        return kwargs

class CreatorListView(ListView):
    model = Creator
    template_name = 'creator/list.html'
    context_object_name = 'creators'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs

class CreatorCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('creator_list')
    template_name = 'creator/add.html'

class CreatorDeleteView(DeleteView):
    model = Creator
    template_name = 'creator/delete.html'
    success_url = reverse_lazy('hero_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'creator/user_edit.html'
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('creator_home')

class CreatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'creator/edit.html'
    model = Creator
    fields = '__all__'