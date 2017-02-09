"""Views for imager_images."""

from imager_images.models import Photo, Album
from django.contrib.auth.mixins import LoginRequiredMixin
from imager_profile.models import UserProfile
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class LibraryView(TemplateView):
    """Class based view for Library."""

    template_name = 'imager_images/gallery.html'

    def get_context_data(self):
        """Show a users galleries and photos."""
        the_user = self.request.user
        user_photos = Photo.objects.filter(photographer=the_user.profile)
        paginator = Paginator(user_photos, 4)
        page = self.request.GET.get('lower')

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        user_albums = Album.objects.filter(owner=the_user.profile)
        paginator1 = Paginator(user_albums, 4)
        page1 = self.request.GET.get('upper')
        try:
            pages1 = paginator1.page(page1)
        except PageNotAnInteger:
            pages1 = paginator1.page(1)
        except EmptyPage:
            pages1 = paginator.page(paginator.num_pages)

        context = {'albums': user_albums, 'lower': pages, 'upper': pages1}
        return context


class AlbumAdd(LoginRequiredMixin, CreateView):
    """Class based view for adding an album."""

    template_name = "imager_images/create.html"
    model = Album
    fields = ['contents',
              'title',
              'description',
              'published',
              'cover_photo']
    success_url = reverse_lazy("library")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """Form should update the photographer to the user."""
        self.object = form.save(commit=False)
        self.object.owner = UserProfile.objects.get(user=self.request.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PhotoAdd(LoginRequiredMixin, CreateView):
    """Class based view for adding a photo."""

    template_name = "imager_images/create.html"
    model = Photo
    fields = ['image_file',
              'title',
              'description',
              'published',
              'tags']

    success_url = reverse_lazy("library")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """Form should update the photographer to the user."""
        self.object = form.save(commit=False)
        self.object.photographer = UserProfile.objects.get(user=self.request.user)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class AlbumEdit(UserPassesTestMixin, UpdateView):
    """Class based view for editing an album."""

    template_name = "imager_images/update.html"
    model = Album
    fields = ['contents',
              'title',
              'description',
              'published',
              'cover_photo']
    success_url = reverse_lazy("library")
    raise_exception = True

    def test_func(self):
        """Override the userpassestest test_func."""
        album = Album.objects.get(pk=self.kwargs['pk'])
        return album.owner.user == self.request.user


class PhotoEdit(UserPassesTestMixin, UpdateView):
    """Class based view for editing a photo."""

    template_name = "imager_images/update.html"
    model = Photo
    fields = ['image_file',
              'title',
              'description',
              'published',
              'tags']
    success_url = reverse_lazy("library")
    raise_exception = True

    def test_func(self):
        """Override the userpassestest test_func."""
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        return photo.photographer.user == self.request.user


class AlbumList(ListView):
    """Class based view for Album list."""

    template_name = "imager_images/albums.html"
    model = Album
    context_object_name = 'albums'
    paginate_by = 4

    def get_queryset(self):
        """Get public albums."""
        return Album.objects.filter(published="PUBLIC")


class PhotoList(ListView):
    """Class based view for Photo list."""

    template_name = "imager_images/photos.html"
    model = Photo
    context_object_name = 'photos'
    paginate_by = 4

    def get_queryset(self):
        """Get public photos."""
        return Photo.objects.filter(published="PUBLIC")


class PhotoTagList(ListView):
    """The list view for tagged photos."""

    template_name = "imager_images/photos.html"
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        """Get queryset class method."""
        return Photo.objects.filter(tags__slug=self.kwargs.get("slug")).all()

    def get_context_data(self, **kwargs):
        """Get context class method."""
        context = super(PhotoTagList, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context


class PhotoDetail(DetailView):
    """Class based view for Photo Detail."""

    template_name = "imager_images/photo_detail.html"
    model = Photo

    def get_context_data(self, **kwargs):
        """Get context class method."""
        photo = Photo.objects.get(id=self.kwargs.get("pk"))
        similar_photos = Photo.objects.filter(
            tags__in=photo.tags.all()
        ).exclude(
            id=self.kwargs.get("pk")
        ).distinct()
        return {"similar_photos": similar_photos, "photo": photo}


class AlbumDetail(ListView):
    """Class based view for Album detail."""

    template_name = 'imager_images/album_detail.html'
    model = Album
    paginate_by = 4

    def get_context_data(self):
        """Get albums and photos and return them."""
        album = Album.objects.get(id=self.kwargs['pk'])
        photos = album.contents.all()

        paginator = Paginator(photos, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return {'album': album, 'photo': pages}
