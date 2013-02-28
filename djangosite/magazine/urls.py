from django.conf.urls import url, patterns

urlpatterns = patterns('djangosite.magazine.views',
    url(r'^(?P<slug>[-\w\/]*)/$', 'article', name='article'),
)