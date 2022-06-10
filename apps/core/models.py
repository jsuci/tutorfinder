from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class CustomUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class CustomUser(AbstractBaseUser):

    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]

    GENDER_TYPE_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female')
    ]

    LEVEL_TYPE_CHOICES = [
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'),
        ('doctoral', 'Doctoral')
    ]

    SUBJECT_TYPE_CHOICES = [
        ('accounting', 'Accounting'),
        ('speech', 'Speech'),
        ('compsci', 'Compsci'),
        ('english', 'English'),
        ('humanities', 'Humanities'),
        ('math', 'Math'),
        ('natsci', 'Natural Science'),
        ('socsci', 'Social Science'),
    ]


    # default fields from AbstractBaseUSer
    email           = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=True, null=True)
    username        = models.CharField(max_length=30, unique=True, blank=True, null=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser	= models.BooleanField(default=False)

    # custom fields
    user_type       = models.CharField(max_length=8, choices=USER_TYPE_CHOICES, blank=True, null=True)

    # basic info
    first_name      = models.CharField(max_length=50, blank=True, null=True)
    last_name       = models.CharField(max_length=50, blank=True, null=True)
    gender          = models.CharField(max_length=1, choices=GENDER_TYPE_CHOICES, blank=True, null=True)
    date_of_birth   = models.DateField(blank=True, null=True)
    mobile_regex    = RegexValidator(regex=r'^0?\d{9,15}$', message="Phone number must be entered in the format: '09xxxxxxxxx'.")
    mobile_number   = models.CharField(validators=[mobile_regex], max_length=17, blank=True, null=True)

    # home address
    address_1       = models.CharField(max_length=128, blank=True, null=True)
    address_2       = models.CharField(max_length=128, blank=True, null=True)
    city            = models.CharField(max_length=64, blank=True, null=True)
    country         = models.CharField(max_length=64, blank=True, null=True)
    postal_code     = models.CharField(max_length=5, blank=True, null=True)


    # qualifications
    school_name     = models.CharField(max_length=128, blank=True, null=True)
    level           = models.CharField(max_length=15, choices=LEVEL_TYPE_CHOICES, blank=True, null=True)
    subject         = models.CharField(max_length=15, choices=SUBJECT_TYPE_CHOICES, blank=True, null=True)
    experience      = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return self.email
        
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin
        
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
