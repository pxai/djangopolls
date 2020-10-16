# Sample django apps

Reminders:
## Django setup
Install django with:

```shell
python -m pip install Django
```

## Create the app
```shell
 django-admin startproject project-name
```

Running the app
```shell
 python manage.py runserver
```
Open site at http://localhost:8000

## Don't forget to add db stuff
```shell
python manage.py migrate

```

### When adding tables

```shell
python manage.py makemigrations polls
python manage.py migrate
```

Try this to see how it does it:

```shell
python manage.py sqlmigrate polls 0001
```

To check for problems:
```shell
 python manage.py check;
 ```

## The shell

Great to try stuff
```shell
python manage.py shell
```
```python
>>>
>>> Question.objects.all()
<QuerySet []>

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
1

>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

>>> q.question_text = "What's up?"
>>> q.save()

>>> Question.objects.all()
```
### Querying
```python
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>
>>> Question.objects.get(id=2)
>>> Question.objects.get(pk=1)  # primary key

>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>


>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```


## Django admin
```shell
python manage.py createsuperuser
```
Then:
```shell
python manage.py runserver
```
And go to admin

### adding Poll to admin

Inside `polls/admin.py`:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## Testing
### Setting up tests for views:
From the shell:
```shell
python manage.py shell
```
```python
from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
>>> response = client.get('/')
Not Found: /

>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
## to get content:
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
```
