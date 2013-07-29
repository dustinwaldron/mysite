from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from contact import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.contact_form),
    url(r'^confirmation/$', views.confirmation),

)