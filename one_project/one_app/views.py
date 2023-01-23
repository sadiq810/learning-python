from django.shortcuts import render
from one_app.models import AccessRecord, Webpage, Topic, Users
from . import forms

#for custom login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list, 'title': "Hello world"}

    return render(request, 'index.html', context=date_dict)

def users(request):
    usersList = Users.objects.order_by('first_name')
    users_dict = {"users_list": usersList}
    return render(request, 'users.html', context=users_dict)

def user_form(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form= forms.UserForm(request.POST)
        if form.is_valid():
            print('Validation success.')
            print("First Name: "+form.cleaned_data['first_name'])
            print("Last Name: "+form.cleaned_data['last_name'])
            print("Email: "+form.cleaned_data['email'])

            Users.objects.create(first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'],
                                        email=form.cleaned_data['email'])

    return render(request, 'form_user.html', {'form': form})

def user_model_form(request):
    form = forms.UserModelForm()
    if request.method == 'POST':
        form= forms.UserModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)

    return render(request, 'form_user.html', {'form': form})

def about(request):
    return render(request, 'about.html', context={'title': "About Page"})

def home2(request):
    print('Home2')
    return render(request, "one_app/index.html")

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)


    dict = {"user_form": forms.UserForm(), "profile_form": forms.UserProfileInfoForm(), "registered": registered}
    return render(request, "one_app/registration.html", context=dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('dashboard')
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'one_app/login.html', {})

@login_required
def dashboard(request):
    return render(request, "one_app/dashboard.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("index")