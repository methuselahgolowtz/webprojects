from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users

def home(request):
    user = Users.objects.all()
    return render(request, "Simple/index.html",{'user':user})


def add_records(request):
    if request.method == "POST":
        first_name = request.POST['fistname']  
        second_name = request.POST['secondname']
        email = request.POST['email']
        location = request.POST['Location']
        user = Users(first_name=first_name, second_name=second_name, email=email, location=location)
        user.save()
        return redirect('/')
    return render(request, "Simple/form.html")

def delete_function(request,id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/')

def upd_info(request, id):
    user = Users.objects.get(id=id)
    return render(request, "Simple/update.html",{'user':user})

def uprecord(request,id):
        first_name = request.POST['fistname']  
        second_name = request.POST['secondname']
        email = request.POST['email']
        location = request.POST['Location']
        user = Users.objects.get(id=id)
        user.first_name = first_name
        user.second_name = second_name
        user.email = email
        user.location = location
        user.save()
        return redirect('/')

