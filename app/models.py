import logging

from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

logger = logging.getLogger(__name__)


class Address(TimeStampedModel):
    user = models.ForeignKey( settings.AUTH_USER_MODEL , null=True, blank=True, on_delete=models.CASCADE)
    street = models.TextField(null=True, blank=True, help_text="Street", db_index=True)
    city = models.TextField(null=True, blank=True, help_text="City", db_index=True)
    state = models.TextField(null=True, blank=True, help_text="State", db_index=True)
    country = models.TextField(null=True, blank=True, help_text="Country", db_index=True)
    pincode = models.TextField(null=True, blank=True, help_text="Country", db_index=True)


    class Meta:
        unique_together = ['user', 'street', 'city', 'state', 'country', 'pincode']
