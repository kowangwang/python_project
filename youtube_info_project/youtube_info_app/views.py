from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from youtube_api_function import get_video_description

def show_overview(request):
    template = loader.get_template('overview.html')
    context = {
        "description":""
    }

    if 'video_url' in request.POST.keys():
        video_url = request.POST['video_url']
        _show_description(context, video_url)

    return HttpResponse(template.render(context, request))

def _show_description(context, video_url=''):
    if video_url:
        context['description'] = get_video_description(video_url)

    return HttpResponseRedirect(reverse('show_overview'))