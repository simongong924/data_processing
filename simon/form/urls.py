from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/$', views.form, name='form'),
    url(r'^submitted/$', views.submitted, name='submitted'),
    url(r'^jobs/(?P<job_number>[a-zA-Z0-9]+)/$', views.report, name='report'),
]