from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns = {
  url(r'^twitter_login/$', views.twitter_login, name='twitter_login'),
  url(r'^twitter_home/$', views.twitter_home, name='twitter_home'),
  url(r'^twitter_logout/$', views.twitter_logout, name='twitter_logout'),
  url(r'^twitter_register/$',views.twitter_register, name='register'),
  url(r'^users_list/$',views.users_list, name='users_list'),
  url(r'^create_post/$',views.create_post, name='create_post'),
  url(r'^(?P<username>[a-z0-9-]+)/(?P<fid>\d+)/$', views.update_followers, name='update_followers'),
  url(r'^(?P<pid>\d+)/$', views.delete_post, name='delete_post'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
