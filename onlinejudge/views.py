from django.shortcuts import render
from .models import Problem

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

    return render(requests, 'submissions.html', {'problems': problems})
