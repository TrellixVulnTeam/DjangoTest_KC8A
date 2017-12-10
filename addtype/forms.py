from django import forms
from .models import *



class CreateTypeForm(forms.ModelForm):

    class Meta:
        model=Type
        exclude=[]

