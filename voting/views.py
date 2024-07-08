from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .algorithm import quick_sort

# Create your views here.

def voter_info(request, candidate_id):

    candidate = get_object_or_404(Candidate, id=candidate_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        voterid = request.POST.get('voterid')
        citizenshipno = request.POST.get('citizenshipno')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        
        try:
            voter = Voter.objects.get(voter_id=voterid, citizenship_no=citizenshipno)

            if voter.vote_casted:
                context = {'error': "You have already casted your vote!"}
                return render(request, 'voting/voter_info.html', context)
            
            candidate.vote_count += 1
            candidate.save()

            voter.vote_casted = True
            voter.save()

            return redirect('results')

        except Voter.DoesNotExist:
            context={'error': "Invalid Voter!!"}
            return render(request, 'voting/voter_info.html', context)

    context={}
    return render(request, 'voting/voter_info.html', context)


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

    csit_candidates = list(Candidate.objects.all())
    quick_sort(csit_candidates, 0, len(csit_candidates) - 1)

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

