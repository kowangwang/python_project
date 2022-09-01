from django.template import loader
from django.http import HttpResponse

def show_overview(request):
    template = loader.get_template('overview.html')
    return HttpResponse(template.render())