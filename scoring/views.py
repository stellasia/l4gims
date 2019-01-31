from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView

from .forms import ActionsForm, QuestionsForm
from .models import Action, Score


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


class ActionNewView(FormView):
    form_class = ActionsForm
    template_name = "scoring/action/new_action.html"

    def get_success_url(self):
        return "/scoring/action/%s"  % self.action.pk
        
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
        self.action = action
        return super().form_valid(form)


class ActionDetailView(DetailView):
    model = Action
    template_name = "scoring/action/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = Score.objects.filter(
            user = self.object.user,
        ).filter(
            Q(current=True) | Q(expected_after_action = self.object)
        )
        context['score_data'] =  [
            s.get_data_for_radar() for s in scores
        ]
        return context


class ActionDeleteView(RedirectView):
    pass