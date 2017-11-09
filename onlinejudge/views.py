from django.shortcuts import render
from .models import Problem, SubmissionForm
#from django.http import HttpResponseRedirect
import os
#from .forms import SubmissionForm
import datetime

def savetofile(nameoffile, data):
    with open(nameoffile, 'w') as submissionfile:
        submissionfile.write(data)
def compare_files(file1,file2):
    with open(file1, "r") as expected_output_file, open(file2, "r") as user_output_file:
        expected_output=expected_output_file.read().rstrip().splitlines()
        user_output=user_output_file.read().rstrip().splitlines()
        print(expected_output)
        print(user_output)
        if (len(expected_output)!=len(user_output)):
                return "Wrong Answer"
        else:
            for i in range (len(user_output)):
                if (user_output[i]!=expected_output[i]):
                    return "Wrong Answer"
        return "Correct Answer"

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
        

    # if this is a POST request we need to process the form data
    if requests.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(requests.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # Collating the data into usable variable names
            cleaned_data=form.cleaned_data
            code = cleaned_data["code"]
            language = cleaned_data["language"]
            problem_id = cleaned_data["problem"].problem_id
            problem = cleaned_data["problem"] 

            obj = form.save(commit=False)
            obj.user = requests.user
            obj.save()
            
            # 1. We construct paths of submission file, input file, expected output file
            submissionfilepath = "submissions/" + str(obj.id) + "." + language
            inputfilepath = "problems/" + str(problem_id) + "/input.txt"
            expectedoutputfilepath = "problems/" + str(problem_id) + "/expected_output.txt"

            # 2. We save the file
            savetofile(submissionfilepath, code)

            # 3. Then we run the program using inputfile as the input and output to a given file.
            print(obj.problem.timelimit)
            os.system("./timeout -t " + str(obj.problem.timelimit) + " -m " + str(obj.problem.memlimit) +" python3 " + submissionfilepath + " < " + inputfilepath + " 1> temp.txt 2> err.txt") 
            #By default, 1> redirects the python output, 2> redirects the error message

            # 3a Check if a timeout occurred, or program failed to compile.
            with open("err.txt") as timeout_file:
                lineone = timeout_file.readline().split()
                print(lineone)
                if lineone[0]=="TIMEOUT":
                    verdict = "Time Limit Exceeded"
                elif lineone[0]=="MEM":
                    verdict="Memory Limit Exceeded"
                elif lineone[0]=="FINISHED":
                    verdict=compare_files(expectedoutputfilepath, "temp.txt")
                else:
                    verdict = "Compilation/Runtime Error"
            # 4. Check if output matches expected output. 
            print(verdict)

            # 5. Create a variable and pass it to the verdicts page. The variable should contain "AC" if the outputs match, or "WA" if they don't. This is sufficient for now. 






            return render(requests, 'verdict.html', {'cleaned_data': cleaned_data, 'verdict' : verdict}) 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()
        return render(requests, 'submissions.html', {'form':form})



