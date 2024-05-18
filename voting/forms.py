from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "username"
                                    }
                                ) 
                            )
    
    first_name = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "first_name"
                                    }
                                ) 
                            )
    
    last_name = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "last_name"
                                    }
                                ) 
                            )
    
    email = forms.EmailField(widget=forms.TextInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "email"
                                    }
                                ) 
                            )
    
    password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "password1"
                                    }
                                ) 
                            )
    
    password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                        'class': "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500",
                                        'id': "password2"
                                    }
                                ) 
                            )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']