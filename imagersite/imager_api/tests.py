"""Test module for imager api buildout."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo
import factory
from django.test import Client, RequestFactory
from django.urls import reverse_lazy
# import datetime


class UserFactory(factory.django.DjangoModelFactory):
    """Create test instance of User Class."""

    class Meta:
        """Invoke user instance using User model class."""

        model = User

    username = factory.Sequence(lambda n: "Photographer {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@theshot.com".format(x.username.replace(" ", ""))
    )


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create test instance of Photo Class."""

    class Meta:
        """Invoke photo instance using Photo model class."""

        model = Photo

    title = factory.Sequence(lambda n: "Photo{}".format(n))


class ApiFrontEndTests(TestCase):
    """Functional and Unit tests for api view."""

    def setUp(self):
        """Test up dummy."""
        self.client = Client()
        self.request = RequestFactory()

        self.users = [UserFactory.create() for i in range(5)]
        self.photos = [PhotoFactory.create() for i in range(5)]

    def user_login(self):
        """New User login."""
        new_user = UserFactory.create()
        new_user.username = 'foo-bar'
        new_user.set_password('wordpass')
        new_user.save()
        return new_user

    def test_api_route_is_status_ok(self):
        """Funcional test for api."""
        new_user = self.user_login()
        self.client.login(username=new_user.username, password='wordpass')
        response = self.client.get(reverse_lazy('api_list'))
        response.user = new_user
        self.assertTrue(response.status_code == 200)

    def test_api_page_renders_correct_html(self):
        """Test authenticated user gets the right html on api."""
        photo = self.photos[0]
        user = self.user_login()
        photo.photographer = user.profile
        photo.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('api_list'))
        self.assertTrue(b"Photo" in response.rendered_content)

    def test_unauthenticated_user_requesting_api(self):
        """Test not logged in user gets an error requesting api."""
        with self.assertRaises(AttributeError):
            self.client.get(reverse_lazy('api_list'))

    def test_one_user_cannot_see_photos_from_other_user(self):
        """Test that one logged in user cannot see the photos of another user in api view."""
        this_photo = self.photos[0]
        this_photo.title = "Joe's Photo"
        this_photo.save()
        this_user = self.users[0]
        this_user.save()
        this_photo.photographer = this_user.profile
        this_photo.save()
        user2 = self.users[1]
        self.client.force_login(user2)
        response = self.client.get(reverse_lazy('api_list'))
        self.assertFalse(b"Joe's Photo" in response.rendered_content)

    def test_other_user_can_see_his_photos(self):
        """Test that the other user can see his own photo."""
        this_photo = self.photos[0]
        this_photo.title = "Joe's Photo"
        this_photo.save()
        this_user = self.users[0]
        this_user.save()
        this_photo.photographer = this_user.profile
        this_photo.save()
        self.client.force_login(this_user)
        response = self.client.get(reverse_lazy('api_list'))
        self.assertTrue(b"Joe's Photo" in response.rendered_content)
