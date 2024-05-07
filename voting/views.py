from django.shortcuts import render
from .models import *

# Create your views here.

def candidate_list(request):
    template_name = 'voting/candidate_list.html'

    csit_candidates = Candidate.objects.filter(desired_position='Head of Department, BSc.CSIT, Kathmandu BernHardt College')

    context = {'csit_candidates': csit_candidates}

    return render(request, template_name, context)

def results(request):
    template_name = 'voting/results.html'

    csit_candidates = Candidate.objects.all()

    context = {'csit_candidates': csit_candidates}

    return render(request, template_name, context)

def candidate_detail(request):
    template_name = 'voting/candidate_detail.html'

    context = {}
    return render(request, template_name, context)

def home(request):
    context = {}

    if request.user.is_authenticated:
        template_name = 'voting/candidate_list.html'
        return render(request, template_name, context)
    else:
        template_name = 'voting/login.html'
        return render(request, template_name, context)

def login(request):
    template_name = 'voting/login.html'
    context = {}
    return render(request, template_name, context)

def guidelines(request):
    template_name = 'voting/guidelines.html'
    context = {}
    return render(request, template_name, context)