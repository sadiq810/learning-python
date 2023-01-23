from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog_app.models import Blog
from blog_app.forms import BlogForm

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', context={"blogs":blogs})

@login_required
def dashboard(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, 'blog/index.html', context={'blogs': blogs})

def detail(request):
    return render(request, 'blog-detail.html')

def newBlog(request):
    print(request.user.id)
    if request.method == "POST":
        form = BlogForm(data=request.POST)
        if form.is_valid():
            #form.user = request.user
            form.save(commit=False)
            form.user_id = request.user.id
            form.slug = 'asdfsdsdsdff'
            form.save()
            return HttpResponseRedirect(reverse('blog_app:dashboard'))

    return render(request, "blog/create.html", {"form": BlogForm()})

def user_login(request):
    msg = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user :
            login(request, user)
            return HttpResponseRedirect(reverse('blog_app:dashboard'))
        else:
            msg = "Invalid Credentials!"

    return render(request, "auth/login.html", context={'message': msg})

def user_register(request):
    msg = ""
    err = ""

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create(username=username, password=password, email=email)
            user.set_password(user.password)
            user.save()

            msg = "User registered successfully."
    except:
        err = "username must be unique."

    return render(request, "auth/register.html", {"message": msg, 'error': err})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))