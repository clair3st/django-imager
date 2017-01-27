"""Setup for deployment."""

from settings import *


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ec2-35-167-175-115.us-west-2.compute.amazonaws.com',
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DATABASE_NAME = 'imager_db'
USER_NAME = 'clairecolin',
DB_PASSWORD = 'W0rdPa88',
HOST = 'imager-app.cwusmhtgws0t.us-west-2.rds.amazonaws.com'


# EMAIL_HOST_PASSWORD

# SECRET_KEY