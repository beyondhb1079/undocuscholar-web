from django.conf.urls import url, include

from . import views

urlpatterns = [
    # ex: /signup/
    url(r'^$', views.index, name='index')
]