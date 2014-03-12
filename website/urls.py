from django.conf.urls import patterns, include, url
from website.views import *
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^news/$', news, name='news'),
    url(r'^team/$', team, name='team'),
    url(r'^fund/$', fund, name='fund'),
    url(r'^resources/$', resources, name='resources'),
    url(r'^join/$', join, name='join'),
    url(r'^fund_tracker/', include('website.fund_tracker.urls', app_name='fund_tracker', namespace='fund_tracker')),
    url(r'^application_portal/', include('website.application_portal.urls', app_name='application_portal', namespace='application_portal'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))