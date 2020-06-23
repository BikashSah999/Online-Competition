from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from dashboard.models import AddCompetition, PhotoContest, StoryContest
# Create your views here.
def home(request):
    active_comps = AddCompetition.objects.filter(status=True)
    params = {'active_comps':active_comps}
    return render(request, "competition_app/index.html", params)

def handlelogin(request):
    if request.method=="POST":
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username = loginusername, password  = loginpassword)
        if user is not None:
            login(request, user)
            messages.info(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.info(request, "User Doesn't Exists.")
            return redirect('/login')
    return render(request, "competition_app/login.html")

def handlesignup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not User.objects.filter(username=username).exists():
            if password1==password2:
                if len(password1)>8:
                    if password1.isalnum():
                        user = User.objects.create_user(username=username, password=password1, email=email)
                        user.save()
                        messages.success(request, "Account Created. Log In to Continue.")
                        return redirect('/login')
                    else:
                        messages.error(request, "Password should be alphanumeric.")
                        return redirect('/signup')
                else:
                    messages.info(request, "Password shoud be atleast 8 characters.")
                    return redirect('/signup')
            else:
                messages.error(request, "Password Doesn't Match.")
                return redirect('/signup')
        else:
            messages.info(request, "Username already exists. Please choose a different username.")
            return redirect('/signup')
    else:
        return render(request, "competition_app/signup.html")

def handlelogout(request):
    logout(request)
    return redirect("/")

def handleform(request, category_name, contest_name):
    if request.user.is_authenticated:
        if category_name=="Story Contest":
            if request.method == 'POST':
                user = request.user.username
                user = User.objects.get(username=user)
                title = request.POST['title']
                story = request.POST['story']
                contest_name = contest_name
                contest_name = AddCompetition.objects.get(title = contest_name)
                post = StoryContest(user=user, title=title, story=story, story_contest_name=contest_name)
                post.save()
                messages.info(request, "Your story has been submitted")
                return redirect('/')
            else:
                contest = contest_name
                params = {'contest':contest}
                return render(request, "competition_app/story_contest_form.html", params)
        
        elif category_name=="Photo Contest":
            contest = contest_name
            params = {'contest':contest}
            return render(request, "competition_app/photo_contest_form.html", params)

    else:
        messages.info(request, "Log In Required")
        return redirect('/')