from django.conf.urls import patterns, include, url
import views 

urlpatterns = patterns('',
    url(r'^$', views.mainpage),
#    url(r'^message/?r=(?<room>\d+)&u=(?<user>\d+)', views.handle_message),
    url(r'^message/r=(?P<room>\d{4})', views.handle_message),
)
