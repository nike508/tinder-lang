from django.conf.urls import url

from . import views

app_name = "meet"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^users/(?P<user_id>[0-9]+)/upvote$', views.upvote_user, name='upvote_user'),
    url(r'^groups/(?P<group_id>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^matches/(?P<match_id>[0-9]+)/?', views.match_detail, name='match_detail'),
    url(r'^users/(?P<user_id>[0-9]+)/match/?', views.match, name='match'),
    url(r'^new_comment/(?P<match_id>[0-9]+)$', views.new_comment, name='new_comment'),
]