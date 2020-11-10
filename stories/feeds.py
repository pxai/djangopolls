from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Story


class LatestStoriesFeed(Feed):
    title = 'My Stories'
    link = reverse_lazy('stories:story_list')
    description = 'New Stories of my page.'

    def items(self):
        return Story.liveStories.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
