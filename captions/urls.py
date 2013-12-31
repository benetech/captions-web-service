from django.conf.urls import patterns, url
from captions import views

#captions URLS

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<youtube_id>\w+)/$', views.youTubeID, name='youtube'),
)
