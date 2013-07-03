from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.blog_page),

)