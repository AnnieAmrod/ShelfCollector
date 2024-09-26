"""
Django settings for shelfCollector project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dotenv
from django.contrib.messages import constants as messages


dotenv.load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG').lower() == 'true'
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'shelfcollector.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Aplicación utilizada para administrar y gestionar sitios web, proporciona un modelo de base de datos para almacenar información sobre diferentes sitios web
    'django.contrib.sites',

    # Aplicaciones descargadas
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'crispy_forms',
    'crispy_bootstrap5',

    # Aplicaciones propias
    'common',
    'usuario',
    'gamesapp',
    'funkosapp',
    'booksapp',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'shelfCollector.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #Para que funcione allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shelfCollector.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurar autenticación utilizando el modelo predeterminado de Django
AUTH_USER_MODEL = 'usuario.Usuario'


AUTHENTICATION_BACKENDS = [
    # Necesaria para realizar el login usando username en el administrador de Django, independiente de django allauth
    'django.contrib.auth.backends.ModelBackend',

    # métodos de autenticación especifica de  `allauth`, como por ejemplo email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Variable de configuración utilizada para especificar el ID del sitio que se está utilizando actualmente. Se utiliza en conjunción con la aplicación 'sites' de Django. Por defecto crea un registro, por ello lo igualamos a 1
SITE_ID = 1

# Variable de configuración utilizada para especificar el nombre del sitio web o aplicación, se utiliza en conjunción con la variable SITE_ID y la aplicación 'sites' de Django para identificar el sitio actualmente en uso y nos sirve para personalizar emails que hacen referencia al nombre del sitio
#SITE_NAME = 'shelfcollector.pythonanywhere.com'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/panel/'
LOGOUT_REDIRECT_URL = '/login/'

#Configuramos el sistema de gestión de usuarios para que requiera una dirección de correo electrónico para el registro y el inicio de sesión, en lugar de requerir un nombre de usuario. Utilizará el email como método de autenticación para el inicio de sesión
#La variable ACCOUNT_USER_MODEL_USERNAME_FIELD se utiliza para especificar el campo del modelo de usuario que se utilizará como nombre de usuario para iniciar sesión. Si se establece en None, indica que el sistema no utilizará un nombre de usuario para iniciar sesión
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#La variable ACCOUNT_EMAIL_REQUIRED especifica si se requiere que los usuarios proporcionen una dirección de correo electrónico al registrarse en el sistema. Si se establece en True, indica que los usuarios deberán proporcionar una dirección de correo electrónico válida para poder registrarse
ACCOUNT_EMAIL_REQUIRED = True
#La variable ACCOUNT_USERNAME_REQUIRED especifica si se requiere que los usuarios proporcionen un nombre de usuario al registrarse en el sistema. Si se establece en False, significa que los usuarios no necesitan proporcionar un nombre de usuario para registrarse
ACCOUNT_USERNAME_REQUIRED = False
#La variable ACCOUNT_AUTHENTICATION_METHOD especifica el método de autenticación que se utilizará para iniciar sesión en el sistema. Si se establece en 'email', significa que los usuarios podrán iniciar sesión utilizando su dirección de correo electrónico en lugar de un nombre de usuario
ACCOUNT_AUTHENTICATION_METHOD = 'email'
#La variable ACCOUNT_EMAIL_VERIFICATION se utiliza para controlar cómo se verifican las direcciones de correo electrónico de los usuarios. Si se establece en 'mandatory', significa que se requiere que todos los usuarios verifiquen su dirección de correo antes de poder iniciar sesión o realizar acciones en la aplicación, se utiliza para evitar que los usuarios introduzcan direcciones de correo no válidas o falsas
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #TODO descomentar cuando haga el tema de los emails


#Configuración que se utiliza para que Django envíe correos electrónicos a través de un servidor de correo electrónico externo, como Gmail, haciendo uso del protocolo SMTP, el cual resulta útil para aplicaciones que necesitan enviar correos electrónicos a sus usuarios, como aplicaciones de comercio electrónico o redes sociales
#La variable EMAIL_BACKEND se utiliza para especificar el backend de correo electrónico que se debe utilizar para enviar correos electrónicos, en este caso, se hace uso del backend de correo electrónico SMTP de Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#La variable EMAIL_HOST se utiliza para especificar el host del servidor de correo electrónico que se está utilizando para enviar emails. En este caso, se está utilizando el servidor de correo electrónico de Gmail
EMAIL_HOST = 'smtp.gmail.com'
#La variable EMAIL_PORT se utiliza para especificar el puerto del servidor de correo electrónico que se está utilizando para enviar correos electrónicos. En este caso, se está utilizando el puerto 587, que es el puerto recomendado para conectarse a servidores de correo electrónico a través de TLS.
EMAIL_PORT = 587
#Las variables EMAIL_HOST_USER y EMAIL_HOST_PASSWORD se utilizan para especificar un nombre de usuario y una contraseña para autenticar la conexión al servidor de correo electrónico. En este caso, se está utilizando una cuenta de correo electrónico de Gmail creada específicamente para enviar correos electrónicos desde la aplicación
EMAIL_HOST_USER = 'avaluappdjango@gmail.com'
EMAIL_HOST_PASSWORD = 'lmqoraagqzitzssz' #AvaluappDjango96!
#EMAIL_USE_TLS se utiliza para especificar si se deben utilizar conexiones seguras (TLS) al enviar correos electrónicos. En este caso, se establece en True, lo que significa que sí se deben utilizar conexiones seguras, lo cual es importante para garantizar la privacidad y seguridad
EMAIL_USE_TLS = True


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración CKEditor
# Información extraída de: github.com/django-ckeditor/django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline''NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft',
            'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Link', 'Unlink', '-', 'RemoveFormat', 'Source']
        ],
        #'width': '235px',
        'height': '160px',
    }
}

MESSAGE_TAGS = {messages.ERROR: 'danger'}

#-------------------- Para que funcionen las plantillas de Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
