from django.shortcuts import render, redirect
from .models import Problem, SubmissionForm
import os
import datetime
from onlinejudge.views_functions import*

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



# redundant view
def index(requests):
    return render(requests, 'index.html', {}) # the third argument is for variables to be passed to the file

# redundant view
def signup(requests):
    return render(requests, 'signup.html', {})

# redundant view
def login(requests):
    return render(requests, 'login.html', {})

def problemset(requests):
    problems = Problem.objects.all()
    return render(requests, 'problemset.html', {'problems' : problems})

def submissions(requests):

    # if this is a POST request we need to process the form data
    if requests.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(requests.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_data = form.cleaned_data
            obj = form.save(commit=False)
            obj.user = requests.user
            obj.save()

            verdict = check_cases(obj)

            # Create a variable and pass it to the verdicts page.

            return render(requests, 'verdict.html', {'cleaned_data': form.cleaned_data, 'verdict' : verdict})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()
        return render(requests, 'submissions.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
