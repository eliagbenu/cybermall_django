from django.conf.urls import patterns, include, url

from computers import views

urlpatterns = patterns('',
    # Examples:
    url(r'^laptops/', 'views.laptops'),

    url(r'^desktops/', 'views.desktops'),
)

