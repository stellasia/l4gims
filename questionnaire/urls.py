from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
    path('apropos/', TemplateView.as_view(template_name="about.html")),
    path('diagnostic/', views.QuestionnaireView.as_view()),
    path('merci/', TemplateView.as_view(template_name="merci.html")),
    path('actions/', TemplateView.as_view(template_name="actions.html")),
    path('stats/', TemplateView.as_view(template_name="stats.html")),

]
