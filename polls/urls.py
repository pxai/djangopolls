from . import views
from django.urls import path

app_name = 'polls'  # now you have to add `polls:` to links
urlpatterns = [
    path('about', views.about, name='about'),
    # manual # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('index_long', views.index_long, name='index_long'),
    # ex: /polls/5/
    # manual # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # manual # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # manual # path('<int:question_id>/vote/', views.vote, name='vote'),
]
