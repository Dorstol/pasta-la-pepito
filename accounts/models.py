from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(
        region="UA",
        unique=True,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into " "this admin site."),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )
    objects = UserManager()

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "phone"

    def __str__(self):
        return str(self.phone)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
