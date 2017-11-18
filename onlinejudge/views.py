from django.shortcuts import render
from .models import Problem, SubmissionForm
import os
import datetime
from onlinejudge.views_functions import*


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







