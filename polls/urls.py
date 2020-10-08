from . import views
from django.urls import path

app_name = 'polls'  # now you have to add `polls:` to links
urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('index_long', views.index_long, name='index_long'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
