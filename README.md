# Guraso django app

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
```
python manage.py shell

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
