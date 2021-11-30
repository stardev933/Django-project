from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from .models import CustomUser,KCalAmount


#############################
# Forms for User Creation / Change
#############################

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ['username','email','phone_number','password1','password2']



class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ("email",)

#############################
# Forms for KCals
#############################

class KCalAmountForm(forms.ModelForm):

	class Meta:
		model = KCalAmount

		# what fields can alter in form
		fields = [
			"amount"
		]
		widgets = {
			'amount':forms.TextInput(attrs={'cols':5,'rows':20,'placeholder':"Input a value."},)
		}

		exclude = ()