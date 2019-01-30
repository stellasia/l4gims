from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import ActionsForm
from .models import Action


class NewActionsView(FormView):
    form_class = ActionsForm
    template_name = "actions.html"
    success_url = '/action/impact/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"user": self.request.user})
        return kwargs
    
    def form_valid(self, form):
        item = form.save()
        item.user = self.request.user
        item.save()
        return super().form_valid(form)


class ActionListView(ListView):
    model = Action
    template_name = "actions_list.html"
