from django import forms

from .models import Questionnaire


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        exclude = ['created_on', 'updated_on',]

    def validate(self, data):
        # TODO: check that number of female is less than number of employees
        # and idem for disabled, etc...
        return data
        
"""    
    company_name = forms.CharField(label="Nom de l'entreprise", max_length=250)

    sector = forms.ChoiceField(
        label="Votre structure appartient...",
        choices=SECTOR,
        widget=forms.RadioSelect
    )
    activity = forms.ChoiceField(
        label="Quel est votre secteur d'activité ?",
        choices=ACTIVITY,
        widget=forms.RadioSelect
    )

    num_employees = forms.IntegerField(
        label="Nombre de salariés au Luxembourg au 1er janvier 2018",
        help_text="(personnes dirigeantes, collaborateurs sous CDD et CDI, travailleurs intérimaires, apprentis, stagiaires, élèves et étudiants inclus)",
        min_value=1,
        max_value=1000000,
    )

    num_employee_female = forms.IntegerField(
        label="Salariés de genre féminin (au total) :",
        min_value=0,
        max_value=1000000,
    )

    num_contract_interim = forms.IntegerField(
        label="Nombre de salariés en intérim : ",
    )
    num_contract_temporary = forms.IntegerField(
        label="Nombre de CDD",
    )
    num_contract_permanent = forms.IntegerField(
        label="Nombre de CDI",
    )
    
    num_employee_disabled = forms.IntegerField(
        label="Nombre de salariés ayant le statut de salariés handicapés :",
    )
    num_employee_redeployed = forms.IntegerField(
        label="Nombre de salariés ayant bénéficié d'un reclassement interne ou externe",
    )
    num_employee_living_in_lux = forms.IntegerField(
        label="Nombre de  salariés residant au Grand-Duché de Luxembourg",
    )
    num_employee_young = forms.IntegerField(
        label="Nombre de salariés de moins de 26 ans",
    )
    num_employee_old = forms.IntegerField(
        label="Nombre de salariés de plus de 50 ans",
    )


    # section 2
    has_diversity_politics = forms.ChoiceField(
        label="Votre structure a-t-elle défini une politique de gestion de la diversité ?",
        choices=YES_NO,
        widget=forms.RadioSelect        
    )
    actions_for_diversity = forms.MultipleChoiceField(
        label="Vos actions en faveur de la diversité concernent:",
        choices=ACTIONS_FOR_DIVERSITY,
        widget=forms.CheckboxSelectMultiple,
    )
    
    # section 3
    process = forms.MultipleChoiceField(
        label="Choisissez dans la liste ci-dessous les processus dont dispose votre entreprise",
        choices=PROCESS,
        widget=forms.CheckboxSelectMultiple,
    )

    # section 4
    work_conditions = forms.ChoiceField(
        label="Votre structure a-t-elle mis en place des conditions de travail favorisant le bien-être des collaborateurs ?",
        choices=WORK_CONDITIONS,
        widget=forms.RadioSelect
    )
"""
