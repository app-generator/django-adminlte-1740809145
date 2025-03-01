# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nevim = models.TextField(max_length=255, null=True, blank=True)
    lastlogin = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Device(models.Model):

    #__Device_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Interface(models.Model):

    #__Interface_FIELDS__
    deviceid = models.ForeignKey(device, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Interface_FIELDS__END

    class Meta:
        verbose_name        = _("Interface")
        verbose_name_plural = _("Interface")



#__MODELS__END
