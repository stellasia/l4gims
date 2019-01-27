import random

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from common.choices import DIVERSITY_TYPE


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
        last_created_users = users.filter(
                date_joined__gte='2018-01-01',
            )
        users_no_form = users.filter(
            )
        users_passive = users.filter(
            last_login__lte='2018-01-15',
        )

        random.seed(13)        
        score_data = [
            [{"axis": d, "value": random.random()} for v, d in DIVERSITY_TYPE]
        ]
        return {
            "last_created_users": last_created_users,
            "users_no_form": users_no_form,
            "users_passive": users_passive,
            "data": score_data,
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
        
        random.seed(12)        
        score_data = [
            [{"axis": d, "value": random.random()} for v, d in DIVERSITY_TYPE]
        ]
        return {
            "user": user,
            "data": score_data,
            }
