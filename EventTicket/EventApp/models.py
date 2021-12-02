from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Min
import re

def validate_code(value):
    if not re.fullmatch(r'^[a-zA-Z]{2}[\/]{1}[0-9]{2}[a-zA-Z]{1}[0-9]{2}[-]{1}[a-zA-Z]{1}[0-9]{2}$', value):
        raise ValidationError('Invalid code')
def validate_price(value):
    if value<0:
        raise ValidationError('Price can`t be less than 0')

class EVENT(models.Model):
    Data = models.DateField()
    Start = models.TimeField()
    End = models.TimeField()
    Price = models.FloatField(validators=[validate_price])
    Code = models.CharField(max_length=12, validators=[validate_code])
    Location = models.CharField(max_length=70)