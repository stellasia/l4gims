from django.db import models

class Actions(models.Model):
    # Nom Action / Type diversité / Processus RH / Date / Texte libre / Statut
    created_on = models.DateTimeField(auto_now_add=True)
    action = models.CharField(unique=True, max_length=128)
    diversity_type = models.CharField(max_length=128)
    processus = models.CharField(unique=True, max_length=128)
    planned_on = models.DateTimeField()
    comment = models.CharField(unique=True, max_length=128)
    status = models.CharField(unique=True, max_length=128)
