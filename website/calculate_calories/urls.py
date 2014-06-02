from django.conf.urls import patterns
from calculate_calories import views
from django.conf.urls import url

urlpatterns = patterns('calculate_calories.views',
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^home/$', views.home , name = "home"),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login , name = "login"),
)