from django.views.generic import TemplateView

# Create your views here.

class GraceView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'im the hero',
            'id': 'My name is Grace Kamenashi',
            'image': '/static/images/SL_Grace.png'
        }

class FirebirdView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'HINOTORI',
            'id': 'My name is Firebird',
            'image': '/static/images/Firebird.png'
        }

class JokerView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'light my way',
            'id': 'My name is Joker Antiphon',
            'image': '/static/images/Joker.png'
        }