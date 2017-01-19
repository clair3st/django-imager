"""Tests for the imager site app."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import UserProfile
import factory


class UserTestCase(TestCase):
    """The User Model test class."""

    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User

        username = factory.Sequence(lambda n: "Photographer {}".format(n))
        email = factory.LazyAttribute(
            lambda x: "{}@theshot.com".format(x.username.replace(" ", ""))
        )

    def setUp(self):
        """The appropriate setup for the appropriate test."""
        self.users = [self.UserFactory.create() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """Test user profile is created at some time as user."""
        self.assertTrue(UserProfile.objects.count() == 20)

    def test_profile_is_associated_with_actual_users(self):
        """Test user profile is affiliated with a user instance."""
        profile = UserProfile.objects.first()
        self.assertTrue(hasattr(profile, "user"))
        self.assertIsInstance(profile.user, User)

    def test_user_has_profile_attached(self):
        """Test the user insance has a profile attached."""
        user = self.users[0]
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, UserProfile)

    def test_active_user_method(self):
        """Test we can detect active users."""
        active_users = UserProfile.active
        self.assertTrue(active_users.count() == 20)

    def test_is_active_user_method(self):
        """Test we can detect active users."""
        profile = UserProfile.objects.first()
        self.assertTrue(profile.is_active)

    def test_inactive_users_are_not_counted_in_active(self):
        """Test inactive users are not in active list."""
        this_user = self.users[0]
        this_user.is_active = False
        this_user.save()
        self.assertTrue(UserProfile.active.count() == User.objects.count() - 1)

    def test_user_has_profile_with_camera(self):
        """Test users have profile with camera options."""
        this_user = self.users[0]
        this_user.camera = 'NIKON'
        this_user.save()
        self.assertTrue(this_user.camera == 'NIKON')

    def test_user_has_profile_with_a_new_camera(self):
        """Test users have profile with camera options."""
        this_user = self.users[0]
        this_user.camera = 'NIKON'
        old_camera = this_user.camera
        this_user.save()
        this_user.camera = 'PHONE'
        this_user.save()
        self.assertFalse(old_camera == this_user.camera)
