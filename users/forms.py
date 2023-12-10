from django import forms 
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email Address', help_text = 'Your university email address.')
    course = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'course', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

class ProfileUpdateForm(forms.ModelForm): 
    date = forms.DateField(label = 'Date of Birth')
    address = forms.CharField(label = 'Address')
    city_town = forms.CharField(label = 'City/Town')
    country = forms.CharField(label = 'Country')
    class Meta:
          model = Profile
          fields = ['date', 'address', 'city_town', 'country', 'image']