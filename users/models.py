from django.db import models

from django.utils import timezone
# get text lazy allows at any point you think data may be translated into user's lang
from django.utils.translation import gettext_lazy

# Create your models here.


# import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

###########################
# Custom user models
# With reference to: 
# https://www.youtube.com/watch?v=Ae7nc1EGv-A
###########################

# Notation: "m" in front = model, then followed by type of field
# camel casing for name of var, snake case for type

# PermissionsMixin allows the user class to get the permissions that dj needs

class CustomUserManager(BaseUserManager):

	def create_superuser(self,email,user_name,password,**other_fields):
		# this is a required field by Django, cannot change name.
		other_fields.setdefault("is_superuser",True)

		other_fields.setdefault("is_staff",True)
		other_fields.setdefault("is_active",True)

		if other_fields.get("is_staff") is not True:
			raise ValueError(
				"Superuser must be assigned to is_staff = True"
			)
		if other_fields.get("is_superuser") is not True:
			raise ValueError(
				"Superuser must be assigned to is_superuser = True"
			)
		
		return self.create_user(email,user_name,password,**other_fields)

	def create_user(self,email,user_name,password,**other_fields):
		# normalize the email by lowercasing domain part

		if not user_name:
			raise ValueError(gettext_lazy("Must provide a username."))

		if not email:
			raise ValueError(gettext_lazy("Must provide email address."))

		email = self.normalize_email(email)
		user = self.model(email=email,user_name=user_name,**other_fields)

		# set the password
		user.set_password(password)
		# save the instance
		user.save()

		return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
	# Authentication of user
	email = models.EmailField(gettext_lazy('email address'),unique = True)
	user_name = models.CharField(max_length=150,unique = True)

	########################
	# User permissions / boolean traits
	########################
	# permissions

	# Django requirements:
	is_staff = models.BooleanField(default = False)
	########################
	# NOTE: You may want an additional step to authenticate users via 
	# email or something else. At the moment, we assume
	# that they are activated from creation.
	#######################
	is_active = models.BooleanField(default= True)

	########################
	# Custom fields
	########################
	is_developer = models.BooleanField(default = True)
	is_pod_plus_member= models.BooleanField(default = True)

	int_points = models.IntegerField(default = 0)	
	int_users_helped = models.IntegerField(default = 0)
	int_days_active = models.IntegerField(default = 0)

	text_about = models.TextField(gettext_lazy(
		'about'),max_length=500,blank = True)

	date_joined = models.DateTimeField(default=timezone.now)
	
	# Defining that we use a custom account manager
	objects = CustomUserManager()

	# USERNAME_FIELD is the default unique field that ID's user
	# This is the unique field that identies users.
	USERNAME_FIELD = "user_name"
	REQUIRED_FIELDS = ["email"]

	def __str__(self):
		return self.user_name
