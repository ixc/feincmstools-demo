from django.conf import settings
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from generic.views import relative_view_on_site_urls

# Seeks all apps' admin declarations
admin.autodiscover()


urlpatterns = patterns('',
    # The admin and its dependencies
    relative_view_on_site_urls, # Makes "view on site" links use relative URLs
    url(r'^admin/', include(admin.site.urls)),
#    To add a blog, uncomment this line, and the two related apps in INSTALLED_APPS.
#    url(r'^blog/', include('djangosite.blog.urls', app_name='blogtools', namespace='blog')),
    url(r'^admin/', include('adminboost.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^accounts/', include(auth_urls)),
    url(r'^markitup/', include('markitup.urls')), #preview view
    url(r'meetups/', include('djangosite.meetups.urls', namespace="meetups")),
#    url(r'^accounts/', include('userena.urls')),
)

# Media/static file serving; only for local development use
if settings.DEBUG:
    # Use glamkit-fallbackserve, to look in a URL for missing media files
    import fallbackserve
    media_pattern = url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip("/"),
        'fallbackserve.views.serve', {'document_root': settings.MEDIA_ROOT})
    urlpatterns += patterns('', media_pattern) + staticfiles_urlpatterns()


"""
Redirects - for legacy urls and e.g. robots.txt
"""
redirect_urls = (
    (r'^robots\.txt$', '%srobots.txt' % settings.STATIC_URL),
    (r'^humans\.txt$', '%shumans.txt' % settings.STATIC_URL),
    (r'^favicon\.ico$', '%sfavicon.ico' % settings.STATIC_URL),
    (r'^apple-touch-icon\.png$', '%s/apple-touch-icon.png' % settings.STATIC_URL), #use '-precomposed' to avoid devices adding glossy effects and rounded corners.
)
 
for oldurl, newurl in redirect_urls:
    urlpatterns += patterns('',
        url(oldurl, 'django.views.generic.simple.redirect_to', {'url': newurl}))

handler500 = 'generic.views.server_error'