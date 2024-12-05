from django.contrib import admin
from django.urls import path, include
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, HeroView, CreatorCreateView, CreatorDeleteView, CreatorDetailView, CreatorListView, CreatorUpdateView, UserUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',   UserUpdateView.as_view(),    name='user_edit'),

    path('',                     HeroView.as_view(), name='home'),
    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path('creator/',                CreatorListView.as_view(),   name='creator_list'),
    path('creator/<int:pk>',        CreatorDetailView.as_view(), name='creator_detail'),
    path('creator/add',             CreatorCreateView.as_view(), name='creator_add'),
    path('creator/<int:pk>/',       UserUpdateView.as_view(),    name='creator_edit'),
    path('creator/<int:pk>/delete', CreatorDeleteView.as_view(), name='creator_delete'),
]
