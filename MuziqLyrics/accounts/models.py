from django.contrib.auth.models import Group, Permission
from django.utils import timezone
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

from MuziqLyrics.accounts.managers import MuziqUserManager


# Create your models here.


class MuziqUser(auth_models.AbstractUser, auth_models.PermissionsMixin):

    username = models.CharField(
        _('username'),
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'username'

    object = MuziqUserManager()

