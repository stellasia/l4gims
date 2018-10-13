from django import forms

class QuestionsForm(forms.Form):
    WORK_CONDITIONS = (
        (1, "Télétravail"),
        (2, "Horaires flexibles"),
        (3, "Autres aménagements pour l’équilibre vie privée/vie professionnelle : temps partiel, congés parentaux, congés sans soldes, absence de réunion après 18h, etc"),
        (4, "Amélioration de la qualité et de l’ergonomie des infrastructures"),
        (5, "Mise en place de services tels que conciergerie, restaurant et crèche d’entreprise, salle de sport, vestiaires, etc."),
    )

    SECTOR = (
        (1, "Au secteur privé"),
        (2, "Au secteur public"),
        (3, "Au secteur associatif"),
    )

    ACTIVITY = (
        (1, "Agriculture, sylviculture et pêche"),
        (2, "Industries extractives"),
        (3, "Industrie manufacturière"),
        (4, "Production et distribution d’électricité, de gaz, de vapeur et d’air conditionné"),
        (5, "Production et distribution d’eau, assainissement, gestion des déchets et dépollution"),
        (5, "Construction"),
        (6, "Commerce, réparation d’automobiles et de motocycles"),
        (7, "Transports et entreposage"),
        (8, "Hébergement et restauration"),
        (9, "Information et communication"),
        (10, "Activités financières et d’assurance"),
        (11, "Activités immobilières"),
        (12, "Activités spécialisées, scientifiques et techniques"),
        (13,"Activités de services administratifs et de soutien"),
        (14,"Enseignement"),
    )

    ACTIONS_FOR_DIVERSITY = (
        (1, "Séniors (plus de 50 ans)"),
        (2, "Jeunes (moins de 26 ans)"),
        (3, "Origine raciale ou ethnique"),
        (4, "Apparence physique"),
        (5, "Maternité"),
        (6, "Handicap"),
        (7, "Etat de santé"),
        (8, "Égalité homme/femme"),
        (9, "Identité sexuelle"),
        (10, "Langues parlées"),
        (11, "Opinions politiques"),
        (12, "Orientation sexuelle"),
        (13, "Ex-détenus / dossier judiciaire"),
        (14, "Niveau de formation"),
        (15, "Équilibre vie professionnelle / vie privée"),
        (16, "Religion ou croyances personnelles"),
        (17, "Lieu de résidence"),
        (18, "Nationalité"),
        (19, "Patronyme"),
        (20, "Appartenance syndicale"),
        (21, "Situation familiale (parentalité, ...)")  ,
    )

    PROCESS = (
        (1, "Descriptif du poste et guide d’entretien basé sur un référentiel de compétences"),
        (2, "Processus de contrôle de non-discrimination dans les annonces de recrutement"),
        (3, "Formation des recruteurs à l’entretien basé sur les compétences"),
        (4, "Formation des personnes en charge du recrutement à la diversité"),
        (5, "Entretien de sortie d’un collaborateur incluant une question liée à la discrimination"),
        (6, "Proposition de stages à des publics susceptibles d’être discriminés"),
        (7, "Participation à des forums/salons de recrutement dédiées à la diversité (exemple : Salon Emploi Handicap)"),
        (8, "Activation de nouveaux réseaux de recrutement"),
        (9, "Partenariats avec des structures dédiées à l’emploi proches des publics discriminés (Adem, associations d’insertions,  associations spécialisées, ..."),
    )

    YES_NO = (
        #(None, "----"),
        (True, "Oui"),
        (False, "Non"),
    )

    
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


    def validate(self, data):
        # TODO: check that number of female is less than number of employees
        # and idem for disabled, etc...
        return data
