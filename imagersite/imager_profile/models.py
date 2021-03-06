"""Create User Profile model."""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible


class IsActiveManager(models.Manager):
    """This returns the active users, manager subclass."""

    def get_queryset(self):
        """Return a list of active users."""
        return super(IsActiveManager, self).get_queryset().filter(
            user__is_active=True
        )


@python_2_unicode_compatible
class UserProfile(models.Model):
    """The library patron and all of its attributes."""

    CAMERAS = (

        ('CANON', "Canon"),
        ('NIKON', "Nikon"),
        ('OLYMPUS', "Olympus"),
        ('SONY', "Sony"),
        ('PANASONIC', "Panasonic"),
        ('PHONE', "Smart Phone"),
        ('', "---Camera Types---"),
    )

    STYLES = (
        ('LANDSCAPE', "Landscape"),
        ('BW', "Black and White"),
        ('PORTRAIT', "Portrait"),
        ('WEDDING', "Wedding"),
        ('SPORTS', "Sports"),
        ('WILDLIFE', "Wildlife"),
        ('URBAN', "Urban"),
        ('TRAVEL', "Travel"),
        ('', "---Photography Styles---"),
        ('LE', 'Long Exposure'),
    )

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )

    camera = models.CharField(max_length=255,
                              choices=CAMERAS,
                              blank=True,
                              null=True)

    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    website = models.URLField(blank=True)
    hireable = models.BooleanField(default=True)
    travel_radius = models.PositiveSmallIntegerField(default=5)
    phone = models.CharField(max_length=12)
    photo_type = models.CharField(max_length=255,
                                  choices=STYLES,
                                  blank=True,
                                  null=True)

    objects = models.Manager()  # the default manager

    active = IsActiveManager()

    def __str__(self):
        """String representation of UserProfile."""
        return self.user.username

    @property
    def is_active(self):
        """Return true if the user is active."""
        return self.user.is_active


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """Make a profile for User."""
    if kwargs["created"]:
        new_profile = UserProfile(user=instance)
        new_profile.save()
