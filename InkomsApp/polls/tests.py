import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question

# Tests.

# Models
class QuestionModelTest(TestCase):
    
    def test_was_published_recentrly_with_future_questions(self):
        """was published_recentrly returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = '¿Quién es el mejor director?', pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)




# Vistas