"""
Модуль содержит модели приложений.
"""
from django.utils import timezone

from django.db import models


class Question(models.Model):
    """ Модель вопроса. """
    name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=200)
    course_id = models.IntegerField(default=0)
    course_module_id = models.IntegerField(default=0)
    tags = models.CharField(max_length=500)
    penalty = models.FloatField(default=1.0)
    publication_date = models.DateTimeField("date published", default=timezone.now)
    changed_date = models.DateTimeField("date changed", default=timezone.now)

    def __str__(self): # pylint: disable=invalid-str-returned

        return self.name

    def get_tags_count(self):
        """ Получает количество тегов вопроса """

        return len(self.tags.split(",")) # pylint: disable=no-member


class QuestionAnswers(models.Model): # pylint: disable=too-few-public-methods
    """ Модель ответа вопроса. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    answer = models.CharField(max_length=500)
    answer_format = models.IntegerField(default=0)
    fraction = models.FloatField(default=1.0)
    feedback = models.CharField(max_length=50, default=0)
    feedback_format = models.IntegerField(default=0)

    def __str__(self): # pylint: disable=invalid-str-returned

        return self.answer
