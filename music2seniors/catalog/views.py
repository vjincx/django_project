from django.shortcuts import render

# Create your views here.
from .models import performer, senior_home, enquiry

def index(request):
    """View function for home page of site."""

    num_performers = performer.objects.all().count()
    num_seniorhomes = senior_home.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_performers': num_performers,
        'num_seniorhomes': num_seniorhomes,

        'num_visits': num_visits,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class performerListView(generic.ListView):
    """Generic class-based view for a list of performers"""
    model = performer

class serniorhomeListView(generic.ListView):
    """Generic class-based view for a list of senior homes"""
    model = senior_home

class PerformerDetailView(generic.DetailView):
    """Generic class-based detail view for a performer."""
    model = performer

class SeniorhomeDetailView(generic.DetailView):
    """Generic class-based detail view for a senior home."""
    model = senior_home



from django.views.generic.edit import CreateView
#from django.urls import reverse_lazy
class EnquiryCreate(CreateView):
    model = enquiry
    fields = ['about', 'first_name', 'last_name', 'inquiry']

class EnquiryDetailView(generic.DetailView):
    """Generic class-based detail view for a senior home."""
    model = enquiry