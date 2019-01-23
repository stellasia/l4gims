import datetime
from django import forms

from .models import Action


class ActionsForm(forms.ModelForm):
    class Meta:
        model = Action
        exclude = ["created_on", ]
        
    # action = forms.CharField(label="Actions (caractériser)", max_length=250)
    # diversity_type = forms.ChoiceField(label="Type de diversité", choices=DIVERSITY_TYPE)

    # processus = forms.ChoiceField(label="Processus RH impliqué", choices=PROCESSUS)
    # planned_on = forms.DateField(initial=datetime.date.today, label="Plannifée pour le")
    # comment = forms.CharField(widget=forms.Textarea, label="Commentaire")
    # status = forms.ChoiceField(label="Statut", choices=STATUS)
