from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from django.http import HttpResponse
from leads.forms import LeadModelForm
from leads.models import Agent, Lead

# Create your views here.

class LeadListView(ListView):
    template_name = "leads/index.html"
    queryset = Lead.objects.all()
    context_object_name= "leads"

class LeadDetailView(DetailView):
    template_name = "leads/show.html"
    queryset = Lead.objects.all()

class LeadCreateView(CreateView):
    template_name="leads/create.html"
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:leads.show", args=(self.object.id,))

class LeadUpdateView(UpdateView):
    template_name="leads/update.html"
    queryset= Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:leads.show",args=(self.object.id,))

class LeadDeleteView(DeleteView):
    template_name="leads/delete.html"
    queryset= Lead.objects.all()

    def get_success_url(sel):
        return  reverse("leads:leads.index")

def home_page(request):
    return render(request,"homepage.html")
