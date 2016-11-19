from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        #preguntar si viene un email y sino viene haremos que mande el error
        # if not email:
        #     raise ValueError('Email debe ser obligatorio')
        email =  self.normalize_email(email)
        user = self.model(username=username, email= email,
                          is_active = True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)

        user.set_password(password)
        user.save(using = self._db)
        return user

    #Creabdo un usuario normal

    def  create_user(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    #Creando un super usuario
    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email= models.EmailField(max_length=50, unique=True)
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField()
    status = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    #intermediario de las transacciones de cada modelo
    objects = UserManager()

    # que atributo se requiere que tome para que se logee
    USERNAME_FIELD = 'username'

    #lista d atributos para crear un usuario
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username



