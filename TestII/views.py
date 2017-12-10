from django.shortcuts import render
from addobject.views import addobject
from addobject.models import Object
from addtype.views import addtype
from addtype.models import *

def main(request):


    Types = Type.objects.all()
    type_list = Types.values_list('name', 'name')
    if request.method =='POST':
            if request.POST['filter']=="all":
                Objects = Object.objects.all()
            else:
                Objects = Object.objects.filter(type=request.POST['filter'])

    else :
       Objects=Object.objects.all()





    return render(request,'main.html',locals())


