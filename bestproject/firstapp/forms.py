from django import forms
from django.conf.urls import url
from django.db.models.base import Model
from django.forms import fields, widgets
from django.contrib.auth.models import User

from .models import Users, Webpages,Userprofile




class ContactForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'



    widgets={

        'firstname':forms.TextInput(),
        'lastname':forms.TextInput(),
        'email':forms.EmailInput(),

    }





class WebForm(forms.ModelForm):
    class Meta:
        model=Webpages
        fields='__all__'


    widgets={


        'topic':forms.TextInput(),
        'name':forms.TextInput(),
        'url':forms.URLInput(),

        }

class FormProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')
        widgets={
            'username':forms.TextInput(),
            'password':forms.PasswordInput(),
            'email':forms.EmailInput(),
        }


class Userprofileinfo(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=('portfolio_site','profile_pic')
        # widgets={

        #     'portfolio_site':forms.URLInput(),
            
            
        # }
