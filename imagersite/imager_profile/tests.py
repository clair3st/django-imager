"""Tests for the imager site app."""
from django.test import TestCase
from django.contrib.auth.models import User
from lender_profile.models import PatronProfile
import factory


class ProfileTestCase(TestCase):
    """The Profile Model test runner."""

    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User

        username = factory.Sequence(lambda n: "Photographer {}".format(n))
        email = factory.LazyAttribute(
            lambda x: "{}@theshot.com".format(x.username.replace(" ", ""))
        )

    def setUp(self):
        """The appropriate setup for the appropriate test."""
        self.foo = "bar"
        self.users = [self.UserFactory.create() for i in range(20)]

    def thing_and_stuff(self):
        self.thing = "stuff"

    def test_profile_is_made_when_user_is_saved(self):
        """."""
        self.thing_and_stuff()
        self.assertTrue(PatronProfile.objects.count() == 20)
        self.assertTrue(self.thing == "stuff")

    def test_profile_is_associated_with_actual_users(self):
        """."""
        profile = PatronProfile.objects.first()
        self.assertTrue(hasattr(profile, "user"))
        self.assertIsInstance(profile.user, User)

    def test_user_has_profile_attached(self):
        """."""
        user = self.users[0]
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, PatronProfile)