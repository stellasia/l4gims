import datetime
from django import forms

from .models import Action


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
