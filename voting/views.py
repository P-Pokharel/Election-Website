from django.shortcuts import render
from .models import *

# Create your views here.

def candidate_list(request):
    template_name = 'voting/candidate_list.html'

    csit_candidates = Candidate.objects.filter(desired_position='Head of Department, BSc.CSIT, Kathmandu BernHardt College')
    print(request.user)

    context = {'csit_candidates': csit_candidates}
    return render(request, template_name, context)

def home(request):
    template_name = 'voting/home.html'
    context = {}
    return render(request, template_name, context)

def results(request):
    template_name = 'voting/results.html'
    context = {}
    return render(request, template_name, context)

def login(request):
    template_name = 'voting/login.html'
    context = {}
    return render(request, template_name, context)

def candidate_detail(request):
    template_name = 'voting/candidate_detail.html'
    context = {}
    return render(request, template_name, context)

def guidelines(request):
    template_name = 'voting/guidelines.html'
    context = {}
    return render(request, template_name, context)