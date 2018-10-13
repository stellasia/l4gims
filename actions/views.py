from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import ActionsForm
from .models import Actions


class NewActionsView(FormView):
    form_class = ActionsForm
    template_name = "actions.html"
    success_url = '/actions/merci/'

    def form_valid(self, form):
        return super().form_valid(form)


class ActionListView(ListView):
    model = Actions
    template_name = "actions_list.html"
