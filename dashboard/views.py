import random

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from common.choices import DIVERSITY_TYPE

from questionnaire.models import Questionnaire
from score.models import Score
from action.models import Action



class DashboardHomeView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        username = user.username
        if "IMS" in user.groups.values_list('name', flat=True):
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

        random.seed(13)        
        score_data = [
            [{"axis": d, "value": random.random()} for v, d in DIVERSITY_TYPE]
        ]
        return {
            "users": users,
            "score_data": score_data,
            }


class DashboardUserView(UserPassesTestMixin, TemplateView):
    template_name = "dashboard_user.html"

    def test_func(self):
        username = self.kwargs.get("username")
        return (self.request.user.username == username
                    or "IMS" in self.request.user.groups.values_list('name', flat=True))
    
    def get_context_data(self, *args, **kwargs):
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)

        q = Questionnaire.objects.filter(
            user=user
        ).first()

        score = Score.objects.filter(
            user=user
        ).last()

        actions = Action.objects.filter(
            user=user,
        )
        past_actions = actions.filter(
            status=Action.COMPLETED,
            )
        ongoing_actions = actions.exclude(
            status=Action.COMPLETED,
        )
        return {
            "user": user,
            "q": q,
            "last_score": score,
            "score_data": score.data() if score else Score.data(),
            "score_evolution_data": None,
            "ongoing_actions": ongoing_actions,
            "past_actions": past_actions,
        }
