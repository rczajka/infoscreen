from django.conf import settings
from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)

if 'django_cas' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^accounts/login/$', 'django_cas.views.login'),
        (r'^accounts/logout/$', 'django_cas.views.logout'),
    )
else:
    urlpatterns += patterns('',
        (r'^accounts/login/$', 'django.contrib.auth.views.login'),
        (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    )

urlpatterns += patterns('',
    url(r'^$', 'infoscreen.views.home', name='home'),
    url(r'^set/$', 'infoscreen.views.set_info', {'slug': 'main'}),
    url(r'^i/(?P<slug>[^/]*)/set/$', 'infoscreen.views.set_info'),
    url(r'^i/(?P<slug>[^/]*)/state/$', 'infoscreen.views.state'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
