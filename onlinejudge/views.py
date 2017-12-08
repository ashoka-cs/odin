from django.shortcuts import render, redirect,  get_object_or_404
from .models import Problem, SubmissionForm, Contest, Submission
import os
import datetime
from onlinejudge.views_functions import*

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



# redundant view
def index(requests):
    return render(requests, 'index.html', {}) # the third argument is for variables to be passed to the file

# redundant view
def login(requests):
    return render(requests, 'login.html', {})

def problemset(requests):
    problems = Problem.objects.all()
    return render(requests, 'problemset.html', {'problems' : problems})

def my_submissions(requests):
    submissions = Submission.objects.filter(user__exact=requests.user)
    print(submissions)
    return render(requests, 'my_submissions.html', {'submissions' : submissions})

def submissions(requests, problem=None):

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
            verdict = check_test_cases(obj)
            obj.verdict = verdict
            obj.save()
            return render(requests, 'verdict.html', {'cleaned_data': form.cleaned_data, 'verdict' : verdict})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm(initial={"problem" : problem})
        return render(requests, 'submissions.html', {'form':form})


def signup(requests):
    if requests.method == 'POST':
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
         #   user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(requests, 'signup.html', {'form': form})


def contestlist(requests):
    contests = Contest.objects.all()
    return render(requests, 'contestlist.html', {'contests': contests})


def contest_detail(requests, contest_pk):
    contest = get_object_or_404(Contest, pk = contest_pk)
        
    start_time=contest.start_time
    end_time=contest.end_time
    running=is_running(start_time,end_time)
    print(running)
    problems=Problem.objects.filter(contest=str(contest_pk))


    return render(requests, 'contest_detail.html', {'contest': contest,'problems': problems,'running': running})


def problem_detail(requests, problem_pk):

    problem = get_object_or_404(Problem, pk = problem_pk)

    if requests.method == 'GET':
        return submissions(requests, problem) #render(requests, 'problem_detail.html', {'problem': problem, 'form': form})
    elif requests.method == 'POST':
        return submissions(requests)