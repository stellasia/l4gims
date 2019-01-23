from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.CurrentStatusView.as_view(), name="score_view"),
    path('compute_from_baro/<int:baro_pk>', views.ComputeScore.as_view(), name="score_compute_from_baro"),
    path('update_after_action/<int:action_pk>', views.UpdateScore.as_view(), name="score_update_after_action"),
    path('after-action/', views.ForecastStatusView.as_view(), name="score_forecast"),
]
