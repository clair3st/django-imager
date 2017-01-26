# django-imager [![Build Status](https://travis-ci.org/clair3st/django-imager.svg?branch=front-end-1)](https://travis-ci.org/clair3st/django-imager)
 simple image management website using Django.

**Authors:** Claire Gatenby and Colin Lamont

##Getting Started

Clone this repository into whatever directory you want to work from.
```
https://github.com/clair3st/django-imager.git
```
Assuming that you have access to Python 3 at the system level, start up a new virtual environment.
```
$ cd django-imager
$ python3 -m venv ENV
$ source ENV/bin/activate
```
Once your environment has been activated, make sure to install Django and all of this project's required packages.
```
(django-imager) $ pip install -r requirements.pip
```
Navigate to the project root, imagersite, and apply the migrations for the app.
```
(django-imager) $ cd imagersite

(django-imager) $ ./manage.py migrate
```
Finally, run the server in order to server the app on localhost
```
(django-imager) $ ./manage.py runserver
```
Django will typically serve on port 8000, unless you specify otherwise. You can access the locally-served site at the address http://localhost:8000.


##Current Models (outside of Django built-ins):

This application allow users to store and organize photos. 

**The `UserProfile` model contains:**

- What type of camera they have (Nikon, iPhone 7, Canon)
- Address
- Bio
- Personal Website
- Hireable
- Travel Radius
- Phone
- Type of Photography (nature, urban, portraits)

The model also supports the following API:

- ImagerProfile.active: provides full query functionality limited to profiles for users who are active (allowed to log in)
- profile.is_active: a property which returns a boolean value indicating whether the user associated with the given profile is active

**The `Photo` model contains:**

- Image_file
- Title
- Description
- Date Uploaded, Date Modified and Date Published
- Photographer - linked to a UserProfile
- Shared or Public

**The `Album` model contains:**

- Contents - Instance of Photo model
- Title
- Description
- Date Uploaded, Date Modified and Date Published
- Owner - linked to a UserProfile
- Shared or Public
- Cover Photo - Photo model


##Current URL Routes

- `/admin` Superuser admin page.
- `/` Home page.
- `/login` Login page.
- `/logout` Logout route, no view.
- `/accounts/register` Register a user form.
- `/accounts/activate/complete/` Activation complete view.
- `/accounts/register/complete/` Registration complete, email sent.
- `/profile` Logged in user's profile view.
- `/profile/<username>` Profile matching <username>.
- `/images/albums` All public photos in imagersite database.
- `/images/photos` All public albums in imagersite database.
- `/images/library` Library of a users photos and albums.
- `/images/albums/<id>` Detail view of album by <id>.
- `/images/photos/<id>` Detail view of photo by <id>.
- `/images/albums/add/` Add a new album.
- `/images/photos/add/` Add a new photo.

##Running Tests

Running tests for the django-imager is fairly straightforward. Navigate to the same directory as the manage.py file and type:
```
(django-imager) $ coverage run manage.py test
```
This will show you which tests have failed, which tests have passed. If you'd like a report of the actual coverage of your tests, type
```
(django-imager) $ coverage report
```
This will read from the included .coverage file, with configuration set in the .coveragerc file. Currently the configuration will show which lines were missing from the test coverage.