from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # <-- after saving a thing, do a thing
from django.dispatch import receiver # <-- listen for thing to be done

# Create your models here.


class UserProfile(models.Model):
    """The library patron and all of its attributes."""
    CANNON = 'CA'
    NIKON = 'NI'
    OLYMPUS = 'OL'
    SONY = 'SO'
    PANASONIC = 'PA'
    PHONE = 'PH'
    CAMERAS = (
        (CANNON, "Cannon"),
        (NIKON, "Nikon"),
        (OLYMPUS, "Olympus"),
        (SONY, "Sony"),
        (PANASONIC, "Panasonic"),
        (PHONE, "Phone"),
    )
    LANDSCAPE = 'LA'
    BW = 'BW'
    PORTRAIT = 'PO'
    WEDDING = 'WE'
    SPORTS = 'SP'
    WILDLIFE = 'WI'
    URBAN = 'UR'
    TRAVEL = 'TR'
    STYLES = (
        (LANDSCAPE, "Landscape"),
        (BW, "Black and White"),
        (PORTRAIT, "Portrait"),
        (WEDDING, "Wedding"),
        (SPORTS, "Sports"),
        (WILDLIFE, "Wildlife"),
        (URBAN, "Urban"),
        (TRAVEL, "Travel"),
    )

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    camera = models.CharField(max_length=255, choices=CAMERAS, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True)
    hireable = models.BooleanField(default=True)
    travel_radius = models.PositiveSmallIntegerField()
    phone = models.CharField()
    photo_type = models.CharField(max_length=255, choices=STYLES, blank=True, null=True)

@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    new_profile = UserProfile(user=instance)
    new_profile.save()
