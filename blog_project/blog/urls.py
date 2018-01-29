from django.conf.urls import url

from blog import views


app_name='blog'

urlpatterns=[
    url(r'^$',views.postlistview.as_view(),name='post_list'),
    url(r'^about/$',views.aboutview.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.postdetailview.as_view(),name='detail'),
    url(r'^post/new/$',views.createpostview.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.updatepostview.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.postdeleteview.as_view(),name='post_delete'),
    url(r'^drafts/$',views.draftlistview.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]