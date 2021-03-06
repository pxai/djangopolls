from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class LiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='live')


class Story(models.Model):
    STATUS_CHOICES = (
        ('empty', 'Empty'),
        ('draft', 'Draft'),
        ('live', 'Live'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='stories')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='empty')

    stories = models.Manager() # The default manager.
    liveStories = LiveManager() # Our custom manager.
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stories:story_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

class Comment(models.Model):
    story = models.ForeignKey(Story,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.story}'
