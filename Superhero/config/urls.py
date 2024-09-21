from django.urls import path
from hero.views import GraceView, FirebirdView, JokerView

urlpatterns = [
    path('',        GraceView.as_view()),
    path('firebird',        FirebirdView.as_view()),
    path('joker',        JokerView.as_view()),
]
