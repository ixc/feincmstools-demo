from django.conf.urls import url, patterns

urlpatterns = patterns('djangosite.meetups.views',
        url(r'^(?P<slug>[-\w\/]*)/$', 'meetup', name='meetup'),
)