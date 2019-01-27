from django import forms

from .models import Questionnaire
from common.choices import *


class QuestionsForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        exclude = ['created_on', 'updated_on',]
        widgets = {
            "actions_for_diversity": forms.CheckboxSelectMultiple(),
            "process": forms.CheckboxSelectMultiple(),
            "work_conditions": forms.CheckboxSelectMultiple(),
            "has_diversity_politics": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs)
        #print(self.fields["work_conditions"].choices)

    def validate(self, data):
        # TODO: check that number of female is less than number of employees
        # and idem for disabled, etc...
        return data
