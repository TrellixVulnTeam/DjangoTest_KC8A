from django.shortcuts import render
from addtype.models import Type
from .forms import *
def addobject(request):
    Types = Type.objects.all()
    a=Types[0]
    form = MyForm(request.POST or None)

    if request.method=="POST" and form.is_valid() :
        data=form.cleaned_data
        if data['max_load']>=0 and data['load']>=0:
            new_form = form.save()
            print(data['name'])
        else:
            print("gkj[jq dtc")


    return render(request,'addobject.html',locals())