from django.conf.urls import patterns, include, url

urlpatterns = patterns('apprtc.views',
    url(r'^$', 'mainpage'),
    url(r'^message/$', 'handle_message'),
)
