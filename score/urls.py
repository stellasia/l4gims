from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.CurrentStatusView.as_view()),    
    path('after-action/', views.ForecastStatusView.as_view()),    
]
