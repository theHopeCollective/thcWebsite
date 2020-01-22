from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    display_name = models.CharField(_('display name'), max_length=30, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=False)
    is_artist = models.BooleanField(_('Are you a Wake County Based Artist?'), default=False)
    is_nonprofit = models.BooleanField(_('Are you representing a Wake County Based Nonprofit looking to benefit our community?'), default=False)

    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD= 'email'
    REQUIRED_FIELDS = ['display_name', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return "@{}".format(self.display_name)

    def get_absolute_url(self):
        return reverse("accounts:user_detail", kwargs={'pk': self.pk}   )

    def email_user(self, subject, message, from_email=None, **kwargs):

        # Sends an email to this User.

        send_mail(subject, message, from_email, [self.email], **kwargs)
