from django.conf.urls import url
from perfis.views import index, exibir

urlpatterns = [
    url(r'^$', index),
    url(r'^perfis$', exibir)
]