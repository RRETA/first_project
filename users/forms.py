from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','is_active', 'is_staff', 'is_superuser','password']
        #fields = "__all__"




class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','is_active', 'is_staff', 'is_superuser','password']
        #fields = "__all__"



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','is_active', 'is_staff', 'is_superuser']
        #fields = "__all__"



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        #fields = "__all__"