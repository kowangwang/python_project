from re import template
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item
from datetime import datetime, date

def show_main_page(request):
    template = loader.get_template('main_page.html')
    my_items = Item.objects.all().values()
    my_items = my_items.order_by('expire_date')

    today = datetime.today()

    # 提醒 - 已過期/快過期
    for item in my_items:
        expire_date = item['expire_date']
        expire_datetime = datetime(expire_date.year, expire_date.month, expire_date.day)
        remind_day = item['remind_day']
        time_diff = (expire_datetime-today).total_seconds()
        if time_diff < -60*60*24:
            expire_status = '已過期'
        elif time_diff < remind_day*60*60*24:   # day to seconds
            expire_status = '快過期'
        else:
            expire_status = ''
        item['expire_status'] = expire_status

    context = {
        'my_items':my_items,
        'today':today
    }

    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['name']
    category = request.POST['category']
    expire_date = request.POST['expire_date']
    remind_day = request.POST['remind_day']
    place = request.POST['place']
    item = Item(
        name=name,
        category=category,
        expire_date=date(int(expire_date[:4]), int(expire_date[4:6]), int(expire_date[6:])),
        remind_day=remind_day,
        place=place
    )
    item.save()

    return HttpResponseRedirect(reverse('show_main_page'))

def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()

    return HttpResponseRedirect(reverse('show_main_page'))

def update(request, id):
    template = loader.get_template('update.html')
    item = Item.objects.get(id=id)
    context = {
        'item':item,
        'expire_date':item.expire_date.strftime('%Y%m%d')   # 到期日顯示方式特別處理
    }

    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name = request.POST['name']
    category = request.POST['category']
    expire_date = request.POST['expire_date']
    remind_day = request.POST['remind_day']
    place = request.POST['place']

    item = Item.objects.get(id=id)
    item.name = name
    item.category = category
    item.expire_date = date(
        int(expire_date[:4]), int(expire_date[4:6]), int(expire_date[6:])
    )
    item.remind_day = remind_day
    item.place = place
    item.save()

    return HttpResponseRedirect(reverse('show_main_page'))