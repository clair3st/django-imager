"""Tests for the imager site app."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import UserProfile
import factory
from django.test import Client, RequestFactory


class UserFactory(factory.django.DjangoModelFactory):
    """Setting up users for tests."""

    class Meta:
        """Set up model."""

        model = User

    username = factory.Sequence(lambda n: "Photographer {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@theshot.com".format(x.username.replace(" ", ""))
    )


class UserTestCase(TestCase):
    """The User Model test class."""

    def setUp(self):
        """The appropriate setup for the appropriate test."""
        self.users = [UserFactory.create() for i in range(20)]

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


class ProfileFrontEndTests(TestCase):
    """Functional and Unit tests for front end views."""

    def setUp(self):
        """Test up dummy."""
        self.client = Client()
        self.request = RequestFactory()

    def test_home_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imagersite.views import home_view
        req = self.request.get("/potato")
        response = home_view(req)
        self.assertTrue(response.status_code == 200)

    def test_home_route_is_status_ok(self):
        """Funcional test."""
        response = self.client.get("/")
        self.assertTrue(response.status_code == 200)

    def test_home_route_uses_right_templates(self):
        """."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "imagersite/base.html")
        self.assertTemplateUsed(response, "imagersite/home.html")

    def test_login_route_status_of_302(self):
        """Test login route redirects status of 302."""
        new_user = UserFactory.create()
        new_user.username = 'foo-bar'
        new_user.set_password('wordpass')
        new_user.save()
        response = self.client.post("/login/", {
            "username": new_user.username,
            "password": 'wordpass'
        })

        self.assertTrue(response.status_code == 302)

    def test_login_route_redirects_home_page(self):
        """Test login route redirects to home page."""
        new_user = UserFactory.create()
        new_user.username = 'foo-bar'
        new_user.set_password('wordpass')
        new_user.save()
        response = self.client.post("/login/", {
            "username": new_user.username,
            "password": 'wordpass'
        }, follow=True)

        self.assertTrue(response.redirect_chain[0][0] == "/")

    def test_login_route_redirects_home_page_no_login(self):
        """Test login route redirects to home page with no login link."""
        new_user = UserFactory.create()
        new_user.username = 'foo-bar'
        new_user.set_password('wordpass')
        new_user.save()
        self.client.post("/login/", {
            "username": new_user.username,
            "password": 'wordpass'
        }, follow=True)
        response = self.client.get("/")
        self.assertFalse('login' in response.content.decode())

    def test_home_page_no_logout_when_not_logged_in(self):
        """Test logout not on homepage."""
        response = self.client.get("/")
        self.assertFalse('logout' in response.content.decode())

    def test_login_has_form(self):
        """Test login has a form."""
        response = self.client.get("/login/")
        self.assertTrue('form' in response.rendered_content)

    def test_registration_has_form(self):
        """Test registration has a form."""
        response = self.client.get("/accounts/register/")
        self.assertTrue('form' in response.rendered_content)

    def register_foo(self, follow=False):
        """Fixture for registration of user."""
        response = self.client.post("/accounts/register/", {
            "username": "Foo1234",
            "email": "foo@bar.com",
            "password1": "tugboats",
            "password2": "tugboats",
        }, follow=follow)
        return response

    def test_register_new_user(self):
        """Test I can register a new user and create an new user model."""
        self.assertTrue(User.objects.count() == 0)
        self.register_foo()
        self.assertTrue(User.objects.count() == 1)

    def test_registered_user_is_inactive(self):
        """Test new created using is not active."""
        self.register_foo()
        the_user = User.objects.first()
        self.assertFalse(the_user.is_active)

    def test_successful_registration_status_302(self):
        """Test registration redirects with 302 status code."""
        response = self.register_foo(follow=False)
        self.assertTrue(response.status_code == 302)

    def test_successful_registration_redirects_to_compelte(self):
        """Test registration redirects to complete."""
        response = self.register_foo(follow=True)
        complete_url = "/accounts/register/complete/"
        self.assertTrue(response.redirect_chain[0][0] == complete_url)

    def test_successful_registration_email(self):
        """Test registration redirects and activation redirects."""
        response = self.register_foo(follow=False)
        key = response.context['activation_key']
        response2 = self.client.get(
            "/accounts/activate/" + key + "/"
        )
        complete = '/accounts/activate/complete/'
        self.assertTrue(response2.url == complete)
