from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(?P<article_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^results/(?P<article_id>[0-9]+)$', views.results, name='results'),
    url(r'^submit/(?P<article_id>[0-9]+)$', views.submit, name='submit'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/(?P<username>[a-zA-z0-9]+)$', views.account, name='account'),
]
