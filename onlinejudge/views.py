from django.shortcuts import render
from .models import Problem
#from django.http import HttpResponseRedirect
import os
from .forms import SubmissionForm
import datetime




# Create your views here.
def index(requests):
    return render(requests, 'index.html', {}) # the third argument is for variables to be passed to the file
def signup(requests):
    return render(requests, 'signup.html', {})
def login(requests):
    return render(requests, 'login.html', {})

def problemset(requests):
    problems = Problem.objects.all()

    return render(requests, 'problemset.html', {'problems' : problems})

def submissions(requests):
    problems = Problem.objects.all()

    # if this is a POST request we need to process the form data
    if requests.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(requests.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            cleaned_data=form.cleaned_data
            date=datetime.datetime.now()
            strdate=str(date).replace(" ","")
            nameoffile="submissions/"+strdate+"."+cleaned_data['language']
            with open(nameoffile, "w") as submissionfile:
                submissionfile.write(cleaned_data['code'])
            if cleaned_data['language']=='py':
                os.system	("python " + nameoffile)
            return render(requests, 'verdict.html', {'cleaned_data': cleaned_data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()
        return render(requests, 'submissions.html', {'form':form})



