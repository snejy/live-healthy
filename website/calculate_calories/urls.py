from django.conf.urls import patterns
from calculate_calories import views
from django.conf.urls import url
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('calculate_calories.views',

    url(r'^home/$', views.home , name = "home"),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login , name = "login"),
    url(r'^logout/$', views.logout , name = "logout"),
    url(r'^profile/$', views.profile , name = "profile"),
    url(r'^track_calories/$', views.track_calories , name = "track_calories"),
    url(r'^about/$', views.about , name = "about"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.home, name = "home"),
)