from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.NewActionsView.as_view()),
    path('merci/', TemplateView.as_view(template_name="merci.html")),
    path('liste/', views.ActionListView.as_view()),
    
]
