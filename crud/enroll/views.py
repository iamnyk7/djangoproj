from django.shortcuts import render,HttpResponseRedirect
from .forms import crudreg
from .models import crud
# Create your views here.
def delpost(request,id):
    if request.method=="POST":
        data=crud.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')

def updatedata(request,id):
    a=False
    if request.method=="POST":
        pi=crud.objects.get(pk=id)
        fm=crudreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            a=True
    else:
        pi=crud.objects.get(pk=id)
        fm=crudreg(instance=pi)
    return render(request,'enroll/update.html',{'fm':fm,'a':a})


def addshow(request):
    a=False
    if request.method=="POST":
        fm=crudreg(request.POST)
        if fm.is_valid():
            title=fm.cleaned_data['title']
            key=fm.cleaned_data['key']
            desc=fm.cleaned_data['desc']
            reg=crud(title=title,key=key,desc=desc)
            reg.save()
            a=True
            fm=crudreg()
        res=crud.objects.all()
        return render(request,'enroll/addshow.html',{'form':fm,'res':res,'a':a})
    else:
        fm=crudreg()
        res=crud.objects.all()
        return render(request,'enroll/addshow.html',{'form':fm,'res':res,'a':a})
