from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	url(r'^$', views.Register.as_view(), name="accounts-register"),
	url(r'^login/$', views.Login.as_view(), name="accounts-login"),
	url(r'^logout/$', views.Logout.as_view(), name="accounts-logout"),
	url(r'^success/$', login_required(views.Success.as_view(), login_url='accounts-login'), name="accounts-success"),
	url(r'^post/(?P<user_id>\d+)/$', views.create, name="posts-create"),
	url(r'^profile/(?P<user_id>\d+)/$', views.show_profile, name="accounts-profile"),
	url(r'^post/delete/(?P<post_id>\d+)/$', views.delete, name="posts-delete"),
	url(r'^post/details/(?P<post_id>\d+)/$', views.show_idea, name="posts-details"),
	url(r'^post/like/(?P<post_id>\d+)/$', views.like_post, name="posts-like"),
]