from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # link user system to user profile
    user = models.OneToOneField(User)

    # additional user info
    ra = models.CharField(max_length=6, blank=False,
                          validators=[RegexValidator(r'^[0-9]*$', message=u'RA invalido, somente numeros permitido'),
                                      MinLengthValidator(6),
                                      MaxLengthValidator(6)],
                          )

    # override unicode to return something readable
    def __unicode__(self):
        return self.ra + ' ' + self.user.username;
