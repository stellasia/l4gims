from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import QuestionsForm


class QuestionnaireView(FormView):
    form_class = QuestionsForm
    template_name = "questionnaire.html"
    success_url = '/ok/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
