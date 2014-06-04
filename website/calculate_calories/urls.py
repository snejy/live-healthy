from django.conf.urls import patterns
from calculate_calories import views
from django.conf.urls import url

urlpatterns = patterns('calculate_calories.views',
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^home/$', views.home , name = "home"),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login , name = "login"),
    url(r'^logout/$', views.logout , name = "logout"),
    url(r'^profile/$', views.profile , name = "profile"),
    url(r'^track_calories/$', views.track_calories , name = "track_calories"),
    url(r'^about/$', views.about , name = "about"),
)