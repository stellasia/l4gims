from django.urls import path

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="scoring/home.html")), #TODO: move this out of scoring app
    path('apropos/', TemplateView.as_view(template_name="scoring/about.html")), #TODO: move this out of scoring app
    path('scoring/measure/', views.QuestionnaireView.as_view(), name="questionnaire"),
    path('scoring/action/new/', views.ActionNewView.as_view(), name="action_new",),
    path('scoring/action/<int:pk>/', views.ActionDetailView.as_view(), name="action_detail",),
    path('scoring/action/delete/<int:pk>', views.ActionDeleteView.as_view(), name="action_delete",),
    path('scoring/action/similarity/', views.ActionSimilarView.as_view(), name="action_sim",),
]
