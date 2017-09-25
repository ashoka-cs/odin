from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html', {}) # the third argument is for variables to be passed to the file
