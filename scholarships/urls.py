from django.conf.urls import url, include

from . import views

urlpatterns = [
    # ex: /scholarships/
    url(r'^$', views.index, name='index'),
    # ex: /scholarships/1
    url(r'^(?P<scholarship_id>[0-9+])/$', views.detail, name='index'),
]