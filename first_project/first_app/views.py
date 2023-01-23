from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello I am from view.py"}
    return render(request, 'index.html', context=my_dict)
#return HttpResponse('Hello world!')

def about(request):
    return render(request, 'about.html', context={'about_info': 'This is about details bro'})
    #return HttpResponse("This is about page.")

def contact(request):
    return render(request, 'first_app/contact.html', context={})
    #return HttpResponse('This is default contact view')

def contactOne(request):
    return render(request, 'first_app/contactOne.html')
    #return HttpResponse("Contact One view.")

def contactTwo(request):
    return render(request, 'first_app/contactTwo.html')
    #return HttpResponse("Contact two view.")