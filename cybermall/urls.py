from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from home import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home'),

    url(r'^computers/', include('computers.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

