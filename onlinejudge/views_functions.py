''' This file defines functions that are called in views.py '''

def save_to_file(name_of_file, data):
    with open(name_of_file, 'w') as submission_file:
        submission_file.write(data)

def compare_files(file1,file2):
    with open(file1, "r") as expected_output_file, open(file2, "r") as user_output_file:

        expected_output = expected_output_file.read().rstrip().splitlines()
        user_output = user_output_file.read().rstrip().splitlines()

        #print(expected_output)
        #print(user_output)

        if (len(expected_output)!= len(user_output)):
                return "Wrong Answer"
        else:
            for i in range (len(user_output)):
                if (user_output[i] != expected_output[i]):
                    return "Wrong Answer"
        return "Correct Answer"
