from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from .forms import ActionsForm, QuestionsForm
from .models import Action


class QuestionnaireView(FormView):
    form_class = QuestionsForm
    template_name = "scoring/questionnaire/questionnaire.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        q = form.save()
        q.user = self.request.user
        q.save()
        q.compute_score()
        return super().form_valid(form)

    def get_success_url(self):
        return "/dashboard/user/%s" % self.request.user.username


class NewActionsView(FormView):
    form_class = ActionsForm
    template_name = "scoring/action/new_action.html"

    def get_success_url(self):
        return "/dashboard/user/%s" % self.request.user.username
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"user": self.request.user})
        return kwargs
    
    def form_valid(self, form):
        action = form.save()
        action.user = self.request.user
        action.save()
        action.update_score()
        return super().form_valid(form)



class ActionDetailView(DetailView):
    model = Action
    template_name = "scoring/action/detail.html"
