import random

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from common.choices import DIVERSITY_TYPE

from scoring.models import Questionnaire, Score, Action
from scoring.utils import get_global_score_for_radar


class DashboardHomeView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        username = user.username
        if "AdminIMS" in user.groups.values_list('name', flat=True):
            return '/dashboard/admin/{username}'.format(username=username)
        return "/dashboard/user/{username}".format(username=username)
    

class DashboardAdminView(UserPassesTestMixin, TemplateView):
    template_name = "dashboard_admin.html"

    def test_func(self):
        username = self.kwargs.get("username")
        return (self.request.user.username == username
                    or "IMS" in self.request.user.groups.values_list('name', flat=True))

    def get_context_data(self, *args, **kwargs):
        users = User.objects.filter(
            groups__name="Customer"
        )

        score_data = get_global_score_for_radar()
        return {
            "users": users,
            "score_data": [score_data, score_data, ],
        }


class DashboardUserView(UserPassesTestMixin, TemplateView):
    template_name = "dashboard_user.html"

    def test_func(self):
        username = self.kwargs.get("username")
        return (self.request.user.username == username
                    or "AdminIMS" in self.request.user.groups.values_list('name', flat=True))
    
    def get_context_data(self, *args, **kwargs):
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)

        q = Questionnaire.objects.filter(
            user=user
        ).first()

        try:
            score = Score.objects.get(
                current=True,
                user=user
            )
        except Score.DoesNotExist:
            score = None

        actions = Action.objects.filter(
            user=user,
        )
        past_actions = actions.filter(
            status=Action.COMPLETED,
        )
        ongoing_actions = actions.exclude(
            status=Action.COMPLETED,
        )

        score_data = score.get_data_for_radar() if score else []
        global_score = get_global_score_for_radar()

        return {
            "user": user,
            "q": q,
            "last_score": score,
            "score_data": [score_data, global_score],
            "evol_data": [{"label": "me",
                           "x": [0, 1, 2, 3, 4, 5, 6],
                           "y": [0, 1, 2, 3, 3.5, 3.7, 5],
                           }],
            "score_evolution_data": None,
            "ongoing_actions": ongoing_actions,
            "past_actions": past_actions,
        }
