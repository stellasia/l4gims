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

    STATUS = (
        (1, "Prévu"),
        (2, "En cours"),
        (3, "Fini"),
    )
    
    action = forms.CharField(label="Actions (caractériser)", max_length=250)
    diversity_type = forms.ChoiceField(label="Type de diversité", choices=DIVERSITY_TYPE)

    processus = forms.ChoiceField(label="Processus RH impliqué", choices=PROCESSUS)
    planned_on = forms.DateField(initial=datetime.date.today, label="Plannifée pour le")
    comment = forms.CharField(widget=forms.Textarea, label="Commentaire")
    status = forms.ChoiceField(label="Statut", choices=STATUS)
