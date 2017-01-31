"""Test module for Models-2 branch, Album and Photo classs buildout."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
import factory
from django.test import Client, RequestFactory
from django.urls import reverse_lazy
import datetime
# Create your tests here.


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


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create test instance of Album."""

    class Meta:
        """Invoke Album instance using Album model class."""

        model = Album

    description = factory.Sequence(lambda n: "Album{}".format(n))
    # cover_photo = SimpleUploadFile(name'test_image.jpg', content=open(IMG_PATH, 'rb').read(), content_type='image/jpeg'))
    title = "Some Image"


class UserTestCase(TestCase):
    """The User Model test class."""

    def setUp(self):
        """The setup and buildout for uses, photos, and albums."""
        self.users = [UserFactory.create() for i in range(20)]
        self.photos = [PhotoFactory.create() for i in range(20)]
        self.albums = [AlbumFactory.create() for i in range(20)]

    def test_photo_exists(self):
        """Test existance of a photo."""
        this_photo = self.photos[0]
        this_photo.save()
        self.assertTrue(self.photos[0])

    def test_photo_has_a_title(self):
        """Test photo had a title (built in tes."""
        this_photo = self.photos[0]
        this_photo.save()
        self.assertTrue(self.photos[0].title)

    def test_photo_has_a_photographer(self):
        """Test photo has a photographer."""
        this_photo = self.photos[0]
        this_photo.save()
        self.assertFalse(self.photos[0].photographer)
        this_user = self.users[0]
        this_user.save()
        this_photo.photographer = this_user.profile
        self.assertTrue(self.photos[0].photographer)

    def test_album_has_a_description(self):
        """Test an album has a description."""
        this_album = self.albums[0]
        this_album.description = "My Album"
        this_album.save()
        self.assertTrue(self.albums[0].description == "My Album")

    def test_album_has_an_owner(self):
        """Test album has a photographer, which is tied to a user."""
        this_user = self.users[0]
        this_user.username = "User 1"
        this_user.save()
        this_album = self.albums[0]
        this_album.owner = this_user.profile
        this_album.save()
        self.assertTrue(self.albums[0].owner.user.username == "User 1")

    def test_album_has_no_contents(self):
        """Test album has no photos in it."""
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.save()
        self.assertTrue(self.albums[0].contents.count() == 0)

    def test_album_has_contents_with_one_photo(self):
        """Test album has one photo in its contents."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.save()
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.contents = [this_photo]
        this_album.save()
        self.assertTrue(self.albums[0].contents.count() == 1)

    def test_album_has_contents_with_two_photos(self):
        """Test album has 2 photos within its contents."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.save()
        next_photo = self.photos[1]
        next_photo.title = "2nd Photo"
        next_photo.save()
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.contents.set([this_photo, next_photo])
        this_album.save()

        self.assertTrue(this_album.contents.count() == 2)

    def test_photo_has_image_file(self):
        """Test photo has an image file associated with it."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.image_file = "happy.png"
        this_photo.save()
        self.assertTrue(self.photos[0].image_file)

    def test_photo_has_description(self):
        """Test photo has a description."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.description = "My Cat Photo"
        this_photo.save()
        self.assertTrue(self.photos[0].description == "My Cat Photo")

    def test_photo_has_date_uploaded(self):
        """Test photo has a date uploaded field."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.date_uploaded = "2017-01-22"
        this_photo.save()
        self.assertTrue(self.photos[0].date_uploaded == "2017-01-22")

    def test_photo_has_date_modified(self):
        """Test photo has a date modified."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.save()
        self.assertTrue(self.photos[0].date_modified == datetime.date.today())

    def test_photo_has_date_published(self):
        """Test photo has a date published."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.date_published = "2017-01-24"
        this_photo.save()
        self.assertTrue(self.photos[0].date_published == "2017-01-24")

    def test_photo_has_published_private(self):
        """Test photo has their published setting as Private."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.published = "PRIVATE"
        this_photo.save()
        self.assertTrue(self.photos[0].published == "PRIVATE")

    def test_photo_has_published_shared(self):
        """Test photo has their published setting as Shared."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.published = "SHARED"
        this_photo.save()
        self.assertTrue(self.photos[0].published == "SHARED")

    def test_photo_has_published_public(self):
        """Test photo has their published setting as Public."""
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.published = "PUBLIC"
        this_photo.save()
        self.assertTrue(self.photos[0].published == "PUBLIC")

    def test_album_has_description(self):
        """Test album has a description."""
        this_album = self.albums[0]
        this_album.title = "My Photo Album"
        this_album.description = "My Cat Photo Album"
        this_album.save()
        self.assertTrue(self.albums[0].description == "My Cat Photo Album")

    def test_album_has_date_uploaded(self):
        """Test album has date uploaded field filled in."""
        this_album = self.albums[0]
        this_album.title = "My Photo Album"
        this_album.date_uploaded = "2017-01-22"
        this_album.save()
        self.assertTrue(self.albums[0].date_uploaded == "2017-01-22")

    def test_album_has_date_modified(self):
        """Test album has a date modified."""
        this_album = self.albums[0]
        this_album.title = "My Photo Album"
        this_album.save()
        self.assertTrue(self.albums[0].date_modified == datetime.date.today())

    def test_album_has_date_published(self):
        """Test album has a date published."""
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.date_published = "2017-01-24"
        this_album.save()
        self.assertTrue(self.albums[0].date_published == "2017-01-24")

    def test_album_has_published_private(self):
        """Test album has their published setting as Private."""
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.published = "PRIVATE"
        this_album.save()
        self.assertTrue(self.albums[0].published == "PRIVATE")

    def test_album_has_published_shared(self):
        """Test album has their published setting as Shared."""
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.published = "SHARED"
        this_album.save()
        self.assertTrue(self.albums[0].published == "SHARED")

    def test_album_has_published_public(self):
        """Test album has their published setting as Public."""
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.published = "PUBLIC"
        this_album.save()
        self.assertTrue(self.albums[0].published == "PUBLIC")


class ProfileFrontEndTests(TestCase):
    """Functional and Unit tests for front end views."""

    def setUp(self):
        """Test up dummy."""
        self.client = Client()
        self.request = RequestFactory()

        self.users = [UserFactory.create() for i in range(5)]
        self.photos = [PhotoFactory.create() for i in range(5)]
        self.albums = [AlbumFactory.create() for i in range(5)]

    def test_album_list_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import AlbumList
        req = self.request.get(reverse_lazy("album_list"))
        view = AlbumList.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_album_list_route_is_status_ok(self):
        """Funcional test for album list."""
        response = self.client.get(reverse_lazy("album_list"))
        self.assertTrue(response.status_code == 200)

    def test_album_list_route_uses_right_templates(self):
        """Test Album list returns the right templates."""
        response = self.client.get(reverse_lazy("album_list"))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/albums.html")

    def test_photo_list_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import PhotoList
        req = self.request.get(reverse_lazy("photo_list"))
        view = PhotoList.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_photo_list_route_is_status_ok(self):
        """Funcional test for photo list."""
        response = self.client.get(reverse_lazy("photo_list"))
        self.assertTrue(response.status_code == 200)

    def test_photo_list_route_uses_right_templates(self):
        """Test photo view uses the correct templates."""
        response = self.client.get(reverse_lazy("photo_list"))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/photos.html")

    def test_album_detail_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import AlbumDetail
        req = self.request.get("/images/albums/11")
        album = self.albums[0]
        album.contents = self.photos
        view = AlbumDetail.as_view()
        response = view(req, pk=album.pk)
        self.assertTrue(response.status_code == 200)

    def test_album_detail_route_is_status_ok(self):
        """Funcional test for album detail."""
        album = self.albums[0]
        response = self.client.get("/images/albums/" + str(album.pk))
        self.assertTrue(response.status_code == 200)

    def test_album_detail_route_uses_right_templates(self):
        """Test album detail uses the correct templates."""
        album = self.albums[0]
        response = self.client.get("/images/albums/" + str(album.pk))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/album_detail.html")

    def test_photo_detail_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import PhotoDetail
        photo = self.photos[0]
        req = self.request.get("/images/photos/" + str(photo.pk))
        view = PhotoDetail.as_view()
        response = view(req, pk=photo.pk)
        self.assertTrue(response.status_code == 200)

    def test_photo_detail_route_is_status_ok(self):
        """Funcional test for photo detail."""
        photo = self.photos[0]
        response = self.client.get("/images/photos/" + str(photo.pk))
        self.assertTrue(response.status_code == 200)

    def test_photo_detail_route_uses_right_templates(self):
        """Test photo detail uses the correct templates."""
        photo = self.photos[0]
        response = self.client.get("/images/photos/" + str(photo.pk))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/photo_detail.html")

    def user_login(self):
        """New User login."""
        new_user = UserFactory.create()
        new_user.username = 'foo-bar'
        new_user.set_password('wordpass')
        new_user.save()
        return new_user

    # def test_library_view_status_ok(self):
    #     """Rendered html has staus 200, Unit Test."""
    #     from imager_images.views import LibraryView
    #     import pdb; pdb.set_trace()
    #     new_user = self.user_login()
    #     self.client.login(username=new_user.username, password='wordpass')
    #     req = self.client.get(reverse_lazy("library"))
    #     req.user = new_user
    #     view = LibraryView.as_view()
    #     response = view(req)
    #     self.assertTrue(response.status_code == 200)

    def test_library_route_is_status_ok(self):
        """Funcional test for library."""
        new_user = self.user_login()
        self.client.login(username=new_user.username, password='wordpass')
        response = self.client.get(reverse_lazy("library"))
        response.user = new_user
        self.assertTrue(response.status_code == 200)

    def test_library_route_uses_right_templates(self):
        """Test library uses the correct templates."""
        new_user = self.user_login()
        self.client.login(username=new_user.username, password='wordpass')
        response = self.client.get(reverse_lazy("library"))
        response.user = new_user
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/gallery.html")

    def test_logged_in_user_sees_their_gallery(self):
        """A logged in user can view their own library."""
        user = UserFactory.create()
        user.save()

        for album in self.albums:
            user.profile.albums.add(album)

        self.client.force_login(user)

        response = self.client.get(reverse_lazy("library"))

        self.assertTrue("Some Image" in str(response.content))

    def test_album_add_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import AlbumAdd
        req = self.request.get(reverse_lazy("album_add"))
        view = AlbumAdd.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_album_add_route_is_status_ok(self):
        """Funcional test for album add."""
        response = self.client.get(reverse_lazy("album_add"))
        self.assertTrue(response.status_code == 200)

    def test_album_add_route_uses_right_templates(self):
        """Test Album add returns the right templates."""
        response = self.client.get(reverse_lazy("album_add"))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/create.html")

    def test_photo_add_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from imager_images.views import PhotoAdd
        req = self.request.get(reverse_lazy("photo_add"))
        view = PhotoAdd.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_photo_add_route_is_status_ok(self):
        """Funcional test for photo add."""
        response = self.client.get(reverse_lazy("photo_add"))
        self.assertTrue(response.status_code == 200)

    def test_photo_add_route_uses_right_templates(self):
        """Test Album add returns the right templates."""
        response = self.client.get(reverse_lazy("photo_add"))
        self.assertTemplateUsed(response, "imagersite/layout.html")
        self.assertTemplateUsed(response, "imager_images/create.html")

    def test_logged_in_user_sees_add_photo_gallery(self):
        """A logged in user can view their own library."""
        user = self.user_login()
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("library"))

        self.assertTrue("Add Photo" and "Add Album" in str(response.content))

    def test_logged_in_user_can_get_to_edit_photo_page(self):
        """Test authenticated user can get to edit photo page."""
        photo = self.photos[0]
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get("/images/photos/" + str(photo.pk) + "/edit/")
        self.assertTrue(response.status_code == 200)

    def test_logged_in_user_can_get_to_edit_album_page(self):
        """Test authenticated user can get to edit album page."""
        album = self.albums[0]
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get("/images/photos/" + str(album.pk) + "/edit/")
        self.assertTrue(response.status_code == 200)

    def test_edit_photo_page_renders_correct_html(self):
        """Test authenticated user gets the right html on edit photo page."""
        photo = self.photos[0]
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get("/images/photos/" + str(photo.pk) + "/edit/")
        self.assertTrue("Save" in response.rendered_content)

    def test_edit_album_page_renders_correct_html(self):
        """Test authenticated user gets correct html on edit album page."""
        album = self.albums[0]
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get("/images/photos/" + str(album.pk) + "/edit/")
        self.assertTrue("Save" in response.rendered_content)

    def test_edit_profile_page_can_get_to_the_page(self):
        """Test authenticated user gets the correct html on edit profile page."""
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("profile_edit"))
        self.assertTrue(response.status_code == 200)

    def test_edit_profile_page_renders_correct_html(self):
        """Test authenticated user gets the correct html on edit profile page."""
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("profile_edit"))
        self.assertTrue("Edit Profile" in response.rendered_content)

    def test_edit_profile_page_has_new_form_fields(self):
        """Test authenticated user sees the new form fields to enter on edit profile page."""
        user = self.user_login()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("profile_edit"))
        self.assertTrue("First Name" in response.rendered_content)
        self.assertTrue("Last Name" in response.rendered_content)
        self.assertTrue("Email" in response.rendered_content)
