from django.conf.urls import patterns, include, url
from main import menu
from main import list1
from main import java
from main import menu_js
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^menu/$', menu),
	('^list1/$', list1),
	('^java/$', java),
    ('^menu_js/$', menu_js),

    # Examples:
    # url(r'^$', 'uchet.views.home', name='home'),
    # url(r'^uchet/', include('uchet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
