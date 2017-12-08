''' This file defines functions that are called in views.py '''
import os
from django.shortcuts import render
import datetime

# For each submission, the verdict is checked for each test case.
def check_test_cases(submission):

    submission_filepath = "submissions/" + str(submission.id) + "." + submission.language
    submission_id = str(submission.id)
    save_to_file(submission_filepath, submission.code)

    problem_id = submission.problem.problem_id
    no_of_test_cases = submission.problem.no_of_test_cases

    timelimit = submission.problem.timelimit
    memlimit = submission.problem.memlimit
    language = submission.language



    for i in range(1, no_of_test_cases + 1):
        input_filepath = "problems/" + str(problem_id) + "/input" + str(i) + ".txt"
        expected_output_filepath = "problems/" + str(problem_id) + "/expected_output" + str(i) + ".txt"

        verdict = check_verdict(submission_filepath, submission_id, input_filepath, expected_output_filepath,
            timelimit, memlimit, language)

        if (verdict != "Correct Answer"):
            break

    print(verdict)
    return verdict


# saves the submitted code to the file 'submission_file'
def save_to_file(name_of_file, data):
    with open(name_of_file, 'w') as submission_file:
        submission_file.write(data)


# runs the submitted code on the system. and redirects the output and the error message to temp. txt and err.txt respectivly
def check_verdict(submission_filepath, submission_id , input_filepath, expected_output_filepath, timelimit, memlimit, language):

    if language == "py":
        os.system("./timeout -t " + str(timelimit) + " -m " + str(memlimit) + " python3 "
            + submission_filepath + " < " + input_filepath + " 1> temp.txt 2> err.txt")

                # By default, 1> redirects the python output, 2> redirects the error message
        return get_verdict("err.txt", expected_output_filepath)


    elif language == ("c"):

        # What is 'r' doing?  What kind of variable is it?
        # Why are we always getting a complilation error?
        #
        r = os.system("gcc -o " + "binaries/" + submission_id + " " + submission_filepath)

        if r != 0:
            return "CE"

        os.system( "./timeout -t " + str(timelimit) + " -m " + str(memlimit) + " binaries/" + submission_id + " < " + input_filepath + " 1> temp.txt 2> err.txt" )

        return get_verdict("err.txt", expected_output_filepath)
    return "LANGUAGE NOT FOUND"



# checks err.txt, and returns the type of error. If there is no error, returns "Correct Answer"
def get_verdict(error_text, expected_output_filepath):

     #  Check if a timeout occurred, or program failed to compile.
    with open(error_text) as timeout_file:
        lineone = timeout_file.readline().split()


        if lineone[0]=="TIMEOUT":
            verdict = "Time Limit Exceeded"
            return verdict
        elif lineone[0]=="MEM":
            verdict = "Memory Limit Exceeded"
            return verdict
        # Check if output matches expected output.
        elif lineone[0]=="FINISHED":
            verdict = compare_files(expected_output_filepath, "temp.txt")

            if (verdict != "Correct Answer"): # the verdict can either be Correct Answer, or Wrong Answer
                return verdict
        else:
            print(lineone[0])
            verdict = "Compilation/Runtime Error"
            return verdict

    return "Correct Answer"


# compares the output of a particular submission with the expected output for the particular problem
def compare_files(file1, file2):
    with open(file1, "r") as expected_output_file, open(file2, "r") as user_output_file:

        expected_output = expected_output_file.read().rstrip().splitlines()
        user_output = user_output_file.read().rstrip().splitlines()

        if (len(expected_output)!= len(user_output)):
                return "Wrong Answer"
        else:
            for i in range (len(user_output)):
                if (user_output[i] != expected_output[i]):
                    return "Wrong Answer"
        return "Correct Answer"

def is_running(start_time,end_time):
    current_time=datetime.datetime.now(datetime.timezone.utc)

    print(current_time)
    if current_time>=start_time and current_time<=end_time:
        running=True
    else:
        running=False
    return running



