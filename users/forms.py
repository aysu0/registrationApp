from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #AddressForm
from .models import Profile 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email Address', help_text = 'Your university email address.')
    date = forms.DateField(label = 'Date Of Birth', help_text = 'Your date of birth.')
    #address = AddressForm()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date', 'email', 'password1', 'password2']

# class AddressForm(AddressForm):
#     street = forms.CharField(max_length=100)
#     city = forms.CharField(max_length=50)
#     postal_code = forms.CharField(max_length=10)
#     country = forms.CharField(max_length=50)
#     fields = ['street', 'city', 'postal_code', 'country']

class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()
    date = forms.DateField(label = 'Date of Birth')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date', 'email']

class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
          model = Profile
          fields = ['image']