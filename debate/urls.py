
from django.conf.urls import url

from debate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^(?P<post_id>[0-9]+)/post/$', views.post_detail, name='post_detail'),
]
