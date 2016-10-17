from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /scholarships/
    url(r'^$', views.collection, name='collection'),
    # ex: /scholarships/1
    url(r'^(?P<scholarship_id>[0-9+])/$', views.detail, name='detail')
]
