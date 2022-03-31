from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import ugettext as _
import datetime

from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        error_messages={'unique': _('A user with that username already exists.')},
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        max_length=150, unique=True, validators=[UnicodeUsernameValidator()], verbose_name='username')
    email = models.EmailField(unique=True, error_messages={'unique': _(
        'A user with this email address already exists.')})
    code = models.CharField(_('code'), max_length=255, null=True, blank=True)
    fullname = models.CharField(
        _("Name"), max_length=255, null=True, blank=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=11, null=True, blank=True)
    address = models.TextField(_('Address'), null=True, blank=True)
    avatar_url = models.ImageField(
        upload_to="images/avatar", null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    account_number = models.CharField(_('Account Number'), max_length=225, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.username

    def is_online(self):
        if self.last_login is not None:
            if self.last_login.date() == datetime.date.today():
                return True
        return False