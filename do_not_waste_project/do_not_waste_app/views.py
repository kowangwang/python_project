from django.template import loader
from django.http import HttpResponse
from .models import Item

def show_main_page(request):
    my_items = Item.objects.all().values()
    my_items = my_items.order_by('expire_date')
    template = loader.get_template('main_page.html')
    context = {
        'my_items':my_items
    }

    return HttpResponse(template.render(context, request))