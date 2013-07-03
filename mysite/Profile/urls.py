from django.conf.urls import patterns, url

from Profile import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$',views.profile_page),

)