from django.conf.urls import patterns, include, url
import views 

urlpatterns = patterns('',
    url(r'^$', views.mainpage),
    url(r'^message/', views.handle_message),
)
