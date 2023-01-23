from django.shortcuts import render
from django.views.generic import ( View, TemplateView, ListView, DetailView,
                                   CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

#Class based view
class CBView(View):
    def get(self, request):
        return HttpResponse("Class based views are cool!")
        #return render(request, 'index.html')

# template view based class
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context



# Detail view and list view
class SchoolListView(ListView):
    #by default variable with data returned to view as school_list, which convert model name to lower and then append _list to it.
    # You can override this variable like below
    #context_object_name = "schools"
    model = models.School

class SchoolDetailView(DetailView):
    #here it just return variable as lower case of the model or you can change it.
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'

#by default will look for school_form.html
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')