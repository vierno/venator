from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fasttracker/',
        include('venator.fasttracker.urls', namespace='fasttracker')),
    url(r'', include('venator.core.urls', namespace='core')),
)
