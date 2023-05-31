"""
Модуль содержит представления приложения.
"""
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .models import Question, QuestionAnswers


class QuestionListView(ListView):
    """ CBV-представление списка вопросов. """
    model = Question


class QuestionDetailView(DetailView):
    """ CBV-представление детальной страницы вопроса. """
    model = Question


class QuestionNewView(CreateView): # pylint: disable=too-many-ancestors
    """ CBV-представление страницы с формой добавления вопроса. """
    model = Question
    fields = "__all__"
    success_url = "/lmsbaikal/"


class QuestionUpdateView(UpdateView): # pylint: disable=too-many-ancestors
    """ CBV-представление страницы с формой редактирования вопроса. """
    model = Question
    fields = "__all__"
    success_url = "/lmsbaikal/"


class QuestionAnswersAddView(CreateView): # pylint: disable=too-many-ancestors
    """ CBV-представление страницы с формой добавления вариантов ответов для вопроса. """
    model = QuestionAnswers
    fields = "__all__"
    success_url = "/lmsbaikal/"
