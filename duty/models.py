from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from accounts import models as acc
# Create your models here.
class Duty(models.Model):
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    DAY_CHOICES = ((MONDAY, 'Monday'),
                   (TUESDAY, 'Tuesday'),
                   (WEDNESDAY, 'Wednesday'),
                   (THURSDAY, 'Thursday'),
                   (FRIDAY, 'Friday'),
                   )
    user = models.ForeignKey(acc.UserProfile())
    horario = models.CharField(max_length=2, validators=[RegexValidator(r'^[0-9]*', message=u'Horario invalido. Formato: HH'),
                                                         MinLengthValidator(2),
                                                         MaxLengthValidator(2)])
    dia = models.CharField(max_length=1,choices=DAY_CHOICES,default=MONDAY)