from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html', {}) # the third argument is for variables to be passed to the file
def signup(requests):
    return render(requests, 'signup.html', {})
def login(requests):
    return render(requests, 'login.html', {})
def problemset(requests):
    return render(requests, 'problemset.html', {})
