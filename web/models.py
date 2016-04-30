from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Entry(models.Model):
    title = models.CharField(_("Title"), max_length=60)
    description = models.TextField(_("Description"), blank=True)
    url = models.URLField(blank=True)
    logo = models.ImageField(blank=True)
    approved = models.BooleanField(_("Approved"), default=False)
    in_dorm = models.BooleanField(_("Is in dormitory?"), default=False)
    added_by = models.ForeignKey(User)

    def __str__(self):
        return self.title
