from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Story


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
                                   status='live',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'stories/story/detail.html',
                  {'story': story})


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
