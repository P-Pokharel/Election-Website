from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

# Create your views here.

def registrationPage(request):

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'voting/registration.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
           
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('candidate_list')

    context = {}
    return render(request, 'voting/login.html', context)

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
        return redirect('candidate_list')
    else:
        return redirect('login')

def guidelines(request):
    template_name = 'voting/guidelines.html'
    context = {}
    return render(request, template_name, context)

