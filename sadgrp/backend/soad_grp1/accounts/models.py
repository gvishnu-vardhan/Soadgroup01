from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
class UserManager(BaseUserManager):
    def create_user(self, email, name,aadharnumber,person, password=None):
        if name is None:
            raise TypeError('Users should have a username')
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,aadharnumber=aadharnumber,person=person)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, aadharnumber, person, password):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, name,aadharnumber,person, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

 

class User(AbstractBaseUser, PermissionsMixin):
   
    email = models.EmailField(max_length=255, unique=True,db_index=True)
    name = models.CharField(max_length=255,unique=True,db_index=True)
    aadharnumber= models.CharField(max_length=12,default='',unique=True)
  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    person = models.IntegerField(default = 0)
    #slugname=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    

   

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','aadharnumber','person']

    
    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }