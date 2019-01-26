from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name="dashboard_home"),
    path('admin/<slug:username>', views.DashboardAdminView.as_view(), name="dashboard_admin"),
    path('user/<slug:username>', views.DashboardUserView.as_view(), name="dashboard_user"),
]
