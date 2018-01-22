from django import forms
from basicapp.models import userprofileinfo
from django.contrib.auth.models import User

#this form made from the User library in auth.models
class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password',)


#this form is the actual copy of model that is created in models.py file...named= userprofileinfo
class profileform(forms.ModelForm):

    class Meta():
        model=userprofileinfo
        fields= ('portfolio_site','profile_pic')



