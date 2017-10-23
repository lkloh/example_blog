
from django.conf.urls import url
from . import views

app_name = 'diary'
urlpatterns = [
	# ex: /diary/5/
	url(r'^$', views.user_list, name='user'),
]
