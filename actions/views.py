from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ActionsForm


class ActionsView(FormView):
    form_class = ActionsForm
    template_name = "actions.html"
    success_url = '/merci/'

    def form_valid(self, form):
        return super().form_valid(form)
