from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.StoryListView.as_view(), name='story_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.story_detail,
        name='story_detail'),
]
