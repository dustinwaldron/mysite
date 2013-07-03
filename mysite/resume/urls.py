from django.conf.urls import patterns, url

from resume import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.resume_page),

)