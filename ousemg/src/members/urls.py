from django.conf.urls import url

from .views import (
	members_create,
	members_detail,
	members_list,
	members_update,
	members_delete,
)

urlpatterns = [
    url(r'^create/$', members_create),
    url(r'^(?P<id>\d+)/$', members_detail, name='detail'),
    url(r'^$', members_list, name='list'),
    url(r'^(?P<id>\d+)/edit/$', members_update, name='update'),
    url(r'^(?P<id>\d+)/delete/', members_delete),
]
