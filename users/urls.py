from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /users/register
    url(r'^register$', views.register, name='register'),
    url(r'^change', views.update, name='update'),
    url(r'^login$', views.login, name='login')
]
