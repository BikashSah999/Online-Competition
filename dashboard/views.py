from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Category, AddCompetition
# Create your views here.
@login_required
def home(request):
    active_comps = AddCompetition.objects.filter(status=True)
    params = {'active_comps':active_comps}
    return render(request, 'dashboard/home.html', params)

def inactive(request):
    inactive_comps = AddCompetition.objects.filter(status=False)
    params = {'inactive_comps':inactive_comps}
    return render(request, 'dashboard/inactive.html', params)

def handlecategory(request):
    if request.method=='POST':
        category_name = request.POST['category']
        if not Category.objects.filter(category=category_name).exists():
            added_by = request.user.username
            add = Category(category=category_name, added_by=added_by)
            add.save()
            messages.info(request, "Category Added Successfully")
            return redirect('dashboardcategory')
        else:
            messages.info(request, "Category already exists")
            return redirect('dashboardcategory')
    else:
        all_cat = Category.objects.all()
        params = {'all_cat':all_cat}
        return render(request, 'dashboard/category.html', params)

def login(request):
    return render(request,'dashboard/login.html')

def delete(request, type, id):
    if type == 'category':
        cat = Category.objects.get(id=id)
        cat.delete()
        messages.info(request,"Category Deleted Successfully")
        return redirect('dashboardcategory')
    if type == 'competition':
        comp = AddCompetition.objects.get(id=id)
        comp.delete()
        messages.info(request, "Competition Deleted Successfully")
        return redirect('dashboardhome')

def edit(request, type, id):
    all_cat = Category.objects.all()
    comp = AddCompetition.objects.get(id=id)
    params = {'comp':comp, 'all_cat':all_cat}
    return render(request, 'dashboard/editcompetition.html', params)

def update(request, id):
    comp = AddCompetition.objects.get(id=id)
    comp.title = request.POST['title']
    cat = request.POST['category']
    cat = Category.objects.get(category=cat)
    comp.category = cat
    comp.description = request.POST['description']
    comp.image = request.FILES['image']
    comp.prize = request.POST['prize']
    comp.status = request.POST['status']
    comp.save()
    messages.info(request, "Competition Updated Successfully")
    return redirect('dashboardhome')

def addcompetition(request):
    if request.method=='POST':
        title = request.POST['title']
        cat = request.POST['category']
        cat = Category.objects.get(category=cat)
        desc = request.POST['description']
        image = request.FILES['image']
        prize = request.POST['prize']
        added_by = request.user.username
        added_by = User.objects.get(username=added_by)
        print (cat)
        add = AddCompetition(title=title, image=image, description=desc, prize=prize, added_by=added_by, category=cat)
        add.save()
        messages.info(request, "Competition Added Successfully")
        return redirect('dashboardhome')
    else:
        all_cat = Category.objects.all()
        params = {'all_cat':all_cat}
        return render(request, 'dashboard/addcompetition.html', params)

def logout(request):
    logout(request)
    return redirect('/')