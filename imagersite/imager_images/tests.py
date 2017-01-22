"""Test module for Models-2 branch, Album and Photo classs buildout."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
import factory

# Create your tests here.


class UserTestCase(TestCase):
    """The User Model test class."""

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

        title = factory.Sequence(lambda n: "Album{}".format(n))

    def setUp(self):
        """The setup and buildout for uses, photos, and albums."""
        self.users = [self.UserFactory.create() for i in range(20)]
        self.photos = [self.PhotoFactory.create() for i in range(20)]
        self.albums = [self.AlbumFactory.create() for i in range(20)]

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
        self.assertFalse(self.albums[0].contents)

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
        import pdb; pdb.set_trace()
        this_photo = self.photos[0]
        this_photo.title = "My Photo"
        this_photo.save()
        next_photo = self.photos[0]
        next_photo.title = "2nd Photo"
        next_photo.save()
        this_album = self.albums[0]
        this_album.title = "My Album"
        this_album.contents.add = this_photo
        this_album.contents.add = next_photo
        this_album.save()
        self.assertTrue(len(self.albums.contents.count) == 2)

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
        this_photo.date_modified = "2017-01-23"
        this_photo.save()
        self.assertTrue(self.photos[0].date_modified == "2017-01-23")

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
        this_album.date_modified = "2017-01-23"
        this_album.save()
        self.assertTrue(self.albums[0].date_modified == "2017-01-23")

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
