import random

from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField

from common.choices import DIVERSITY_TYPE


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True)
    expected_after_action = models.ForeignKey("action.Action", null=True, on_delete=models.CASCADE)
    values = JSONField()
    current = models.BooleanField(default=False)

    def data(self, seed=123, rep=1):
        random.seed(seed)
        score_data = [
            [{"axis": d, "value": random.random()} for v, d in DIVERSITY_TYPE]
            for _ in range(rep)
        ]
