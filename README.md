# django-imager
 simple image management website using Django.


##Models:
This application allow users to store and organize photos. The UserProfile model contains:

- What type of camera they have (Nikon, iPhone 7, Canon?)
- Address
- Bio
- Personal Website
- Hireable
- Travel Radius
- Phone
- Type of Photography (nature, urban, portraits?)

The model also supports the following API:

- ImagerProfile.active: provides full query functionality limited to profiles for users who are active (allowed to log in)
- profile.is_active: a property which returns a boolean value indicating whether the user associated with the given profile is active