from django.shortcuts import render
from .forms import  CreateTypeForm
from django.db.models import *
import django.apps
from addtype.models import Type

def addtype(request):
    form=CreateTypeForm(request.POST or None)
    if request.method=="POST" :
        new_form=form.save()
        print(form.cleaned_data)


    Types=Type.objects.all()
   # for type in Types:

    #    print(type.name)
    return render(request,'addtype.html',locals())