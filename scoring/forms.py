import datetime
from django import forms
from common.choices import *

from .models import Action, Questionnaire


class ActionsForm(forms.ModelForm):
    class Meta:
        model = Action
        exclude = ["created_on", "user"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # Pop the user off the kwargs passed in
        super().__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super().save(commit=False)
        m.user = self.user
        if commit:
            m.save()
        return m


class QuestionsForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        exclude = ['created_on', 'updated_on', 'user']
        widgets = {
            # "actions_for_diversity": forms.CheckboxSelectMultiple(),
            # "process": forms.CheckboxSelectMultiple(),
            # "work_conditions": forms.CheckboxSelectMultiple(),
            "has_diversity_politics": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # Pop the user off the kwargs passed in
        super().__init__(*args, **kwargs)
        #print(self.fields["work_conditions"].choices)

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super().save(commit=False)
        m.user = self.user
        if commit:
            m.save()
        return m
        
    def clean(self):
        return super().clean()
    
