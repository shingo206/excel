from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Sales(models.Model):
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    amount = models.IntegerField()
