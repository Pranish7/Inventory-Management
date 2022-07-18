# from django.db import models  
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
# from django.utils import timezone  
# # from django.utils.translation import gettext_lazy as _  
# from .managers import CustomUserManager  

# # Create your models here.  

# class CustomUser(AbstractBaseUser, PermissionsMixin):  
#     username = None  
#     email = models.EmailField(unique=True, max_length = 200)  
#     date_joined = models.DateTimeField(default=timezone.now)  
#     is_staff = models.BooleanField(default=False)  
#     is_active = models.BooleanField(default=True)  

#     USERNAME_FIELD = 'email'  
#     REQUIRED_FIELDS = []  

#     objects = CustomUserManager()  

#     def has_perm(self, perm, obj=None):  
#         "Does the user have a specific permission?"  
#         # Simplest possible answer: Yes, always  
#         return True  

#     def is_staff(self):  
#         "Is the user a member of staff?"  
#         return self.staff  

#     @property  
#     def is_admin(self):  
#         "Is the user a admin member?"  
#         return self.admin  

#     def __str__(self):  
#         return self.email 





from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from .managers import * 

class CustomUserManager(BaseUserManager):

    def create_user(self,username, first_name, middle_name, last_name, contact_no, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            contact_no = contact_no,
            # group = extra_fields.get('group'),
        )

        user.set_password(password)
        #set password in built for password
        user.save(using=self._db)
        return user

    def create_superuser(self,username, first_name, middle_name, last_name, contact_no, email, password):

        user = self.create_user(
            email = self.normalize_email(email),
            #normalize email makes capital email small
            username = username,
            password = password,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            contact_no = contact_no,
            # group = group,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google','email': 'email'}


class CustomUser(AbstractUser):
    GENDER_TYPE_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('prefer not to mention','prefer not to mention')
    )
    username = models.CharField(max_length=30, unique = True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    contact_no = models.IntegerField(null=True, blank=True)
    email = models.EmailField(("Email Address"), max_length=254, unique=True)
    gender=models.CharField(max_length=30, choices=GENDER_TYPE_CHOICES, default=False)
    photo=models.ImageField(upload_to='img/',null=True, blank=True,default = 'img/None/no-img.jpg')
    # group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name', 'contact_no', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True