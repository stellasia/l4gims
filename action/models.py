from django.conf import settings
from django.db import models

from common.choices import DIVERSITY_TYPE


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

    STATUS = (
        (1, "Prévu"),
        (2, "En cours"),
        (3, "Fini"),
    )
    
    # Nom Action / Type diversité / Processus RH / Date / Texte libre / Statut
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(unique=True, max_length=128)
    diversity_type = models.IntegerField(choices=DIVERSITY_TYPE)
    processus = models.IntegerField(choices=PROCESSUS)
    planned_on = models.DateField()
    comment = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS)
