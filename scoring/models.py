import random
from collections import OrderedDict
from datetime import date
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
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
    )

    num_employee_female = models.IntegerField(
        verbose_name="Salariés de genre féminin (au total) :",
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
    
    def compute_score(self):
        d = Score.random_data()
        Score.objects.create(
            user = self.user,
            expiration_date = date.today()+relativedelta(year=1),
            values = d,
            current = True,
        )    


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True)
    expected_after_action = models.ForeignKey("scoring.Action", null=True, on_delete=models.CASCADE)
    values = JSONField()
    current = models.BooleanField(default=False)

    @classmethod
    def random_data(self, seed=123, rep=1):
        #random.seed(seed)
        score_data = dict( (d, random.random()) for k, d in DIVERSITY_TYPE)
        return OrderedDict(( sorted(score_data.items())))
    
    @property
    def global_score(self):
        if not self.values:
            return 0
        s = 0
        for k, v in self.values:
            s += v
        return s / len(self.values)

    def get_score_dict(self):
        s = self.values
        return s

    def get_sorted_score_values(self):
        return OrderedDict(sorted(self.values.items()))

    def get_data_for_radar(self):
        data = self.get_sorted_score_values()
        return [
            {"axis": k, "value": v} for k, v in data.items()
            ]

    def badges(self):
        pass


class Action(models.Model):

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

    PLANED = 1
    ONGOING = 2
    COMPLETED = 3
    STATUS = (
        (PLANED, "Prévu"),
        (ONGOING, "En cours"),
        (COMPLETED, "Fini"),
    )
    
    # Nom Action / Type diversité / Processus RH / Date / Texte libre / Statut
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    diversity_type = models.IntegerField(choices=DIVERSITY_TYPE)
    processus = models.IntegerField(choices=PROCESSUS)
    planned_on = models.DateField()
    comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS)

    def update_score(self):
        score = Score.objects.get(user=self.user, current=True)
        score_data = score.get_score_dict()
        d = self.get_diversity_type_display()
        current_score_diversity = score_data.get(d)
        new_score_diversity = current_score_diversity * 1.1
        score_data[d] = new_score_diversity
        Score.objects.create(
            user = self.user,
            expected_after_action = self,
            expiration_date = self.planned_on + relativedelta(month=3),
            current = False,
            values = score_data,
        )
