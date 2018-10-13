from django import forms
import datetime

class ActionsForm(forms.Form):
    DIVERSITY_TYPE = (
        (1, "Genre"), 
        (2, "Générationnel"),
        (3, "Culturel"),
        (4, "Handicap"),
    )

    PROCESSUS = (
        (1, "Gestion des effectifs (entrées - sorties)"),
        (2, "Intégration & culture"),
        (3, "Formation"),
        (4, "Evaluation"),
        (5, "Promotion"),
        (6, "Rémunération"),
        (7, "Temps de travail"),
        (8, "Communication"),
        (9, "Participation"),
        (10, "Relations professionnelles"),
    )

    action = forms.CharField(label="Actions (caractériser)", widget=forms.Textarea)
    diversity_type = forms.ChoiceField(label="Type de diversité", choices=DIVERSITY_TYPE, widget=forms.RadioSelect)

    processus = forms.ChoiceField(label="Processus RH", choices=PROCESSUS, widget=forms.RadioSelect)
    planned_on = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    comment = forms.CharField(widget=forms.Textarea)
    status = forms.CharField(widget=forms.Textarea)
