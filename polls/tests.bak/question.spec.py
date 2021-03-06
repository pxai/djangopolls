from django.test import TestCase
from .models import Question
from django.utils import timezone

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="Sample", pub_date=timezone.now())

    def test_question_has_text(self):
        """Animals that can speak are correctly identified"""
        question = Question.objects.get(question_text="Sample")

        self.assertEqual(question.question_text, "Sample")
