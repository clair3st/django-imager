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
        this_user.profile.camera = 'NIKON'
        this_user.save()
        self.assertTrue(self.users[0].profile.camera == 'NIKON')

    def test_user_has_profile_with_a_new_camera(self):
        """Test user who changes camera type updates test db with new camera."""
        this_user = self.users[0]
        this_user.profile.camera = 'NIKON'
        old_camera = this_user.profile.camera
        this_user.save()
        this_user.profile.camera = 'PHONE'
        this_user.save()
        self.assertFalse(old_camera == self.users[0].profile.camera)

    def test_user_has_profile_with_photo_style(self):
        """Test user has a profile with a style of photography selected from choices."""
        this_user = self.users[0]
        this_user.profile.photo_type = 'WILDLIFE'
        this_user.save()
        self.assertTrue(self.users[0].profile.photo_type == 'WILDLIFE')

    def test_user_has_profile_with_address(self):
        """Test user profile with address has address in test db."""
        this_user = self.users[0]
        this_user.profile.address = '123 Cherry Lane, Seattle WA 98101'
        this_user.save()
        self.assertTrue(self.users[0].profile.address == '123 Cherry Lane, Seattle WA 98101')

    def test_user_profile_with_address_does_not_have_blank_addess(self):
        """Test user profile with address doesn't have blank address in test db."""
        this_user = self.users[0]
        this_user.profile.address = 'WILDLIFE'
        this_user.save()
        self.assertFalse(self.users[0].profile.address is None)

    def test_user_has_profile_with_bio(self):
        """Test user has a profile with a bio."""
        this_user = self.users[0]
        this_user.profile.bio = 'I take beautiful pictures. You should hire me.'
        this_user.save()
        self.assertTrue(self.users[0].profile.bio == 'I take beautiful pictures. You should hire me.')

    def test_user_has_profile_with_website(self):
        """Test user has a profile with a website."""
        this_user = self.users[0]
        this_user.profile.website = 'http://www.photoloco.com'
        this_user.save()
        self.assertTrue(self.users[0].profile.website == 'http://www.photoloco.com')

    def test_user_has_profile_is_hirable_by_default(self):
        """Test user has a profile is hireable by default."""
        this_user = self.users[0]
        this_user.save()
        self.assertTrue(self.users[0].profile.hireable is True)

    def test_user_has_profile_is_not_hirable(self):
        """Test user has a profile isn't hireable when set in test db."""
        this_user = self.users[0]
        this_user.profile.hireable = False
        this_user.save()
        self.assertTrue(self.users[0].profile.hireable is False)

    def test_user_profile_has_default_travel_radius(self):
        """Test user profile has a default travel radius of 5."""
        this_user = self.users[0]
        this_user.save()
        self.assertTrue(self.users[0].profile.travel_radius == 5)

    def test_user_profile_has_travel_radius_of_15(self):
        """Test user profile has a travel radius of 15 in test db."""
        this_user = self.users[0]
        this_user.profile.travel_radius = 15
        this_user.save()
        self.assertTrue(self.users[0].profile.travel_radius == 15)

    def test_user_profile_has_phone_number(self):
        """Test user profile has a phone number in test db."""
        this_user = self.users[0]
        this_user.profile.phone = "206-555-1212"
        this_user.save()
        self.assertTrue(self.users[0].profile.phone == "206-555-1212")
