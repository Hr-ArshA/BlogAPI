
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from extentions.name_fixer import upload_img_path
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(_('username'), max_length=256, unique=True)
    photo = models.ImageField(_('Profile Photo'), upload_to=upload_img_path, blank=True, null=True)
    biography = models.TextField(_('bio'), blank=True, null=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    
    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Profile'


@receiver(post_save, sender=CustomUser)
def make_profile(sender, instance, created, **kwargs) -> None:
    if created:
        user = instance
        Profile.objects.create(user=user, username=str(user.email).split('@')[0]).save()


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()