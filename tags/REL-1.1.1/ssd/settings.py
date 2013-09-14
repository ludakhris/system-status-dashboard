# The following two lines are required if an error occurs when creating the Django admin
# account after running syncdb for the first time.  If the error occurs, delete the database
# uncomment these two lines and run syncdb again.  You may comment these out after, if desired
import os
os.environ['LANG'] = 'en_US.UTF-8'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Database information
DATABASES = {
    'default': {
        'ENGINE'  : '',
        'NAME'    : '',         
        'USER'    : '',       
        'PASSWORD': '', 
        'HOST'    : '',
        'PORT'    : '',         
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'ssd.main.context_processors.prefs',
)

ROOT_URLCONF = 'ssd.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ssd.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'ssd.main'
)


#### SSD SPECIFIC CONFIGURATION ####

# All of these settings should be changed in local_settings.py and
# not here, otherwise they'll be overridden if an upgrade is performed

# Maximum uploaded file size (in MB)
MAX_FILE_SIZE = 1

# Show the NAV Header
NAV = True

# Set to the full URL of the desired logo
# LOGO = ''

# If set to True, the 'Report Incident' tab will appear in the nav.
# If you have this set to true, you should also show the NAV header
# If this is not set to True, the view will not work and will 
# give the user an error
REPORT_INCIDENT = True

# If set to True, the 'Contacts' tab will appear in the NAV header
# You will need to complete the contacts template with your specific information
# If this is not set to True, the view also will not work and will 
# give the user an error
CONTACTS = True

# Email Notifications:
# * If set to True, then email notifications will be enabled
#   for incident creation (by admins) and incident reports (by users)
#
# * If set to True, ensure that you have properly set the email options
#   in the application configuration
#
# * If set to False and 'Broadcast Email' is selected during incident
#  creation or a user reports an incident, no email will be sent.
NOTIFY = True

# App Version
APP_VERSION = '1.1.1'

# SSD Url
# This URL will appear on any links back to SSD 
# (e.g. links in email communication sent from SSD)
SSD_URL = ''

# Load custom settings - must point to the local_settings.py file and
# may not be a relative path.
execfile('$__local_dir__$/local_settings.py')