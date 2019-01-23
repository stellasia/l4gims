import random

from django.shortcuts import redirect
from django.views.generic import TemplateView

from common.choices import DIVERSITY_TYPE
from .models import Score



class ComputeScore(TemplateView):
    template_name = ""

    def get(self, *args, **kwargs):
        # get questionnaire
        baro_pk = kwargs.get("baro_pk")

        # compute and save score

        # redirect
        return redirect("score_view")


class UpdateScore(TemplateView):
    template_name = ""

    def get(self, *args, **kwargs):
        # get action
        action_pk = kwargs.get("action_pk")

        # compute and save score

        # redirect
        return redirect("score_view")


class CurrentStatusView(TemplateView):
    template_name = "current_status.html"

    def get_context_data(self):
        context = super().get_context_data()

        random.seed(13)
        
        context["data"] = [
            [{"axis": d, "value": random.random()} for v, d in DIVERSITY_TYPE]
            for _ in range(2)
            ]
        return context


class ForecastStatusView(TemplateView):
    template_name = "forecast.html"
