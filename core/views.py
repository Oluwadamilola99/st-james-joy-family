from django.views.generic import TemplateView

# Create your views here.
class Soon(TemplateView):
    template_name = 'core/coming-soon.html'