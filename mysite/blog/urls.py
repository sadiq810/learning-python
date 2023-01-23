from django.urls import path
from blog.views import AboutView, PostListView, PostDetailView, CreatePostView, \
    PostUpdateView, PostDeleteView, DraftListView, add_comment_to_post, comment_approve, comment_remove, post_publish

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', CreatePostView.as_view(), name='post_new'),
    path('post/(?<str:pk>\d+)/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/(?<str:pk>\d+)/remove', PostDeleteView.as_view(), name='post_remove'),
    path('drafts', DraftListView.as_view(), name='post_draft_list'),
    path('post/(?<str:pk>\d+)/comment', add_comment_to_post, name='add_comment_to_post'),
    path('comment/(?<str:pk>\d+)/approve', comment_approve, name='comment_approve'),
    path('comment/(?<str:pk>\d+)/remove', comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish', post_publish, name='post_publish'),
    #path('post/<str:pk>', PostListView.as_view(), name='post_list'),
    path('about', AboutView.as_view(), name='about')
]