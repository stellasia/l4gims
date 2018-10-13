from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
    path('apropos/', TemplateView.as_view(template_name="about.html")),
    path('barometre/', views.QuestionnaireView.as_view()),
    path('ok/', TemplateView.as_view(template_name="ok.html")),
]
