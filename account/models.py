import email
from multiprocessing.dummy import Manager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError ('User must have username')

        user = self.model(
            Email =self.normalize_email(email),
            Username=username,
            First_Name=first_name,
            Last_Name=last_name,
            
        )

        user.setpassword(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,first_name,last_name,username,phone_number,password,email):
        user = self.create_user(

            Email = self.normalize_email(email),
            First_Name = first_name,
            Last_Name = last_name,
            Username = username,
            Phone_Number =phone_number,
            Password = password
            
        )

        user.is_admin =True
        user.is_active  =True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=250,unique=True)
    phone_number = models.CharField(max_length=50,unique=True)
    notes=models.CharField(max_length=50,null=True,blank=True)


    #required

    date_joined = models.DateTimeField(auto_now_add=True)
    is_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['username','first_name','last_name','phone_number']

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True