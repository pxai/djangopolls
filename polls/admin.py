from django.contrib import admin
from .models import Question, Choice, Comment

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # moar compact
    model = Choice
    extra = 3


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline, CommentInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Comment)
