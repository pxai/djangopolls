from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Story, Comment
# from .forms import EmailStoryForm, CommentForm
from django import forms
from taggit.models import Tag

class EmailStoryForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

def story_list(request):
    object_list = Story.liveStories.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)
    return render(request,
                 'stories/story/list.html',
                 {'page': page,
                  'stories': stories})


def story_detail(request, year, month, day, story):
    story = get_object_or_404(Story, slug=story,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of active comments for this story
    comments = story.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.story = story
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar stories
    story_tags_ids = story.tags.values_list('id', flat=True)
    similar_stories = Story.published.filter(tags__in=story_tags_ids)\
                                  .exclude(id=story.id)
    similar_stories = similar_stories.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'stories/story/detail.html',
                  {'story': story,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_stories': similar_stories})


class StoryListView(ListView):
    queryset = Story.liveStories.all()
    context_object_name = 'stories'
    paginate_by = 3
    template_name = 'stories/story/list.html'

def story_share(request, story_id):
    story = get_object_or_404(Story, id=story_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailStoryForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            story_url = request.build_absolute_uri(story.get_absolute_url())
            subject = f"{cd['name']} recommends you read {story.title}"
            message = f"Read {story.title} at {story_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True

    else:
        form = EmailStoryForm()
    return render(request, 'stories/story/share.html', {'story': story,
                                                    'form': form,
                                                    'sent': sent})
