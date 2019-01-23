from django.db import models
from django.contrib.postgres.fields import JSONField

from common.choices import DIVERSITY_TYPE


class Score(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True)
    expected_after_action = models.ForeignKey("action.Action", null=True, on_delete=models.CASCADE)
    values = JSONField()
    current = models.BooleanField(default=False)
