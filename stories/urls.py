from django.urls import path
from . import views
from .feeds import LatestStoriesFeed

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.story_list, name='story_list'),
    # path('', views.StoryListView.as_view(), name='story_list'),
    path('tag/<slug:tag_slug>/', views.story_list, name='story_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:story>/',
        views.story_detail,
        name='story_detail'),
    path('<int:story_id>/share/', views.story_share, name='story_share'),
    path('feed/', LatestStoriesFeed(), name='story_feed'),
]
