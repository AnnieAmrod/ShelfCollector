from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioPersonalizado(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        usuario = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre, password, **extra_fields)


class Usuario(AbstractBaseUser):
    email = models.EmailField(
                    verbose_name='Email',
                    unique=True,
                    null=False,
                    blank=False)  # Requerido base de datos y formularios
    nombre = models.CharField(
                    max_length=25,
                    verbose_name='Nombre',
                    null=False,
                    blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    objects = UsuarioPersonalizado()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
