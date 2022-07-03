from django import forms
from .models import users
class usersform(forms.ModelForm):
    class Meta:
        model = users
        fields = ['OwnerName','PetName','PetType','Email','City']