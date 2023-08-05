from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from my.models import studentdata
from my.forms import addrecord


def read(request):
    j='ok'
    ob=studentdata.objects.all()
    ob2=None
    if request.method=="POST" and 'item' in request.POST:
        item=request.POST['item'][0]

        ob=studentdata.objects.filter(name__istartswith=item)
        if len(ob)==0:
            j="none"
            ob2=studentdata.objects.all()
        


    
    return render(request,"index.html",{'ob':ob,'j':j,'ob2':ob2})


def create(request):
    fm=addrecord()
    if request.method=="POST":
        fm=addrecord(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']

            studentdata(name=name,email=email).save()
            messages.success(request,"Record Inserted Successfully")
            return redirect('/')
    return render(request,"addrecord.html",{"fm":fm})

def update(request,id):
    ob=studentdata.objects.get(id=id)
    l=[]
    for i in studentdata.objects.all():
        l.append(i.email)

    

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']

        if email in l:
            if email==ob.email:
                messages.success(request,"Nothing is Updated")
                return redirect('/')
            else:
                messages.error(request,"Email Already Exists")
                return redirect('/'+ str(id))
        else:
            studentdata(id=id,name=name,email=email).save()
            messages.success(request,"Record Updated Successfully")
            return redirect('/')
    
    return render(request,"editrecord.html",{"ob":ob})


def delete(request,id):
    studentdata(id=id).delete()
    messages.success(request,"Record Deleted Successfully")
    return redirect('/')







        
    

