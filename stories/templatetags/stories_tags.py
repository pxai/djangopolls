from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
from ..models import Story

register = template.Library()

@register.simple_tag
def total_stories():
    return Story.liveStories.count()

@register.inclusion_tag('stories/story/latest_stories.html')
def show_latest_posts(count=5):
    latest_stories = Story.liveStories.order_by('-publish')[:count]
    return {'latest_stories': latest_stories}

@register.simple_tag
def get_most_commented_stories(count=5):
    return Story.liveStories.annotate(
               total_comments=Count('comments')
           ).order_by('-total_comments')[:count]
