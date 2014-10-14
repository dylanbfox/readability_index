from django.conf.urls import patterns, url
from scores import views

urlpatterns = patterns('',
    url(r'^$', views.display_scores, name='display_scores'),
)
