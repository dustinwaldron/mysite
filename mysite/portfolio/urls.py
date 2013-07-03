from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.portfolio_page),

)