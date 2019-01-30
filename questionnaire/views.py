from django.urls import reverse
from django.views.generic.edit import FormView

from .forms import QuestionsForm


class QuestionnaireView(FormView):
    form_class = QuestionsForm
    template_name = "questionnaire.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        item = form.save()
        item.user = self.request.user
        item.save()
        self.created_item_pk = item.pk
        return super().form_valid(form)

    def get_success_url(self):
         return reverse('score_compute_from_baro',
                        kwargs={'baro_pk': self.created_item_pk}
                        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
