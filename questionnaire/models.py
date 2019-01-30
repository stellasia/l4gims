import random
from django.conf import settings
from django.db import models
#from django.contrib.postgres.fields import ArrayField
from array_field_select.fields import ArrayField

from common.choices import *


class Questionnaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    sector = models.IntegerField(
        verbose_name="Votre structure appartient...",
        choices=SECTOR,
    )
    activity = models.IntegerField(
        verbose_name="Quel est votre secteur d'activité ?",
        choices=ACTIVITY,
    )

    num_employees = models.IntegerField(
        verbose_name="Nombre de salariés au Luxembourg au 1er janvier 2018",
        help_text="(personnes dirigeantes, collaborateurs sous CDD et CDI, travailleurs intérimaires, apprentis, stagiaires, élèves et étudiants inclus)",
        # min_value=1,
        # max_value=1000000,
    )

    num_employee_female = models.IntegerField(
        verbose_name="Salariés de genre féminin (au total) :",
        # min_value=0,
        # max_value=1000000,
    )

    num_contract_interim = models.IntegerField(
        verbose_name="Nombre de salariés en intérim : ",
    )
    num_contract_temporary = models.IntegerField(
        verbose_name="Nombre de CDD",
    )
    num_contract_permanent = models.IntegerField(
        verbose_name="Nombre de CDI",
    )

    num_employee_disabled = models.IntegerField(
        verbose_name="Nombre de salariés ayant le statut de salariés handicapés :",
    )
    num_employee_redeployed = models.IntegerField(
        verbose_name="Nombre de salariés ayant bénéficié d'un reclassement interne ou externe",
    )
    num_employee_living_in_lux = models.IntegerField(
        verbose_name="Nombre de  salariés residant au Grand-Duché de Luxembourg",
    )
    num_employee_young = models.IntegerField(
        verbose_name="Nombre de salariés de moins de 26 ans",
    )
    num_employee_old = models.IntegerField(
        verbose_name="Nombre de salariés de plus de 50 ans",
    )

    # section 2
    has_diversity_politics = models.IntegerField(
        verbose_name="Votre structure a-t-elle défini une politique de gestion de la diversité ?",
        choices=YES_NO,
        default=0,
    )
    actions_for_diversity = ArrayField(
        models.IntegerField(
            choices=ACTIONS_FOR_DIVERSITY,
        ),
        verbose_name="Vos actions en faveur de la diversité concernent:",
    )
    
    # section 3
    process = ArrayField(
        models.IntegerField(
            choices=PROCESS,
        ),
        verbose_name="Choisissez dans la liste ci-dessous les processus dont dispose votre entreprise",
    )

    # section 4
    work_conditions = ArrayField(
        models.IntegerField(
            choices=WORK_CONDITIONS,
        ),
        verbose_name="Votre structure a-t-elle mis en place des conditions de travail favorisant le bien-être des collaborateurs ?",
    )


    @property
    def completed(self):
        return True
        r = random.random()
        print(r)
        return r > 0.5
