from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import Meetup

def meetup(request, slug):

    context = RequestContext(request)
    meetup = get_object_or_404(Meetup, slug=slug)
    context['meetup'] = meetup

    return render_to_response('meetups/meetup.html', context)