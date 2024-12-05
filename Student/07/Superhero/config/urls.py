from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, HeroView, CreatorCreateView, CreatorDeleteView, CreatorDetailView, CreatorListView, CreatorUpdateView, UserUpdateView, CreatorHomeView, logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',   UserUpdateView.as_view(),    name='user_edit'),
    path('logout_user', logout_user, name='logout'),

    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path('',                        RedirectView.as_view    (url='creator/home')),
    path('creator/',                CreatorListView.as_view(),   name='creator_list'),
    path('creator/home',            CreatorHomeView.as_view(),   name='creator_home'),
    path('creator/<int:pk>',        CreatorDetailView.as_view(), name='creator_detail'),
    path('creator/add',             CreatorCreateView.as_view(), name='creator_add'),
    path('creator/<int:pk>/',       CreatorUpdateView.as_view(), name='creator_edit'),
    path('creator/<int:pk>/delete', CreatorDeleteView.as_view(), name='creator_delete'),
]
