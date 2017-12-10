from django import forms
from .models import *
from django.forms.widgets import *


class MyForm(forms.ModelForm):
    class Meta:
        model=Object
        exclude=["over_load"]

    def save(self):

        data=self.cleaned_data
        if data['load']<=data['max_load']:
            over=0
        else: over=(data['load']-data['max_load'])*100/data['max_load']

        obj = Object.objects.create(name=data['name'],
                                       type=data['type'],
                                       max_load=data['max_load'],
                                       load=data['load'],
                                       over_load=over

                                       )
        obj.save()