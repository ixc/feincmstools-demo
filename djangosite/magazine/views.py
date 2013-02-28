from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import Article

def article(request, slug):

    context = RequestContext(request)
    article = get_object_or_404(Article, slug=slug.rstrip('/'))
    context['article'] = article

    return render_to_response('magazine/article.html', context)