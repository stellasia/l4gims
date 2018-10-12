from django.shortcuts import render
from django.views.generic import TemplateView

class QuestionnaireView(TemplateView):
    template_name = "questionnaire.html"
