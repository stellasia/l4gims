from django import forms

class QuestionsForm(forms.Form):
    WORK_CONDITIONS = (
        (1, "Télétravail"),
        (2, "Horaires flexibles"),
        (3, "Autres aménagements pour l’équilibre vie privée/vie professionnelle : temps partiel, congés parentaux, congés sans soldes, absence de réunion après 18h, etc"),
        (4, "Amélioration de la qualité et de l’ergonomie des infrastructures"),
        (5, "Mise en place de services tels que conciergerie, restaurant et crèche d’entreprise, salle de sport, vestiaires, etc."),
    )
    
    company_name = forms.CharField(label="Nom de l'entreprise", max_length=250)

    work_conditions = forms.ChoiceField(label="Votre structure a-t-elle mis en place des conditions de travail favorisant le bien-être des collaborateurs ?", choices=WORK_CONDITIONS)
