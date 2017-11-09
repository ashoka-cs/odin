from django import forms
from .models import Problem

class SubmissionForm(forms.Form):
	problems = Problem.objects.values_list('problem_id','problem_title')
	code = forms.CharField(label="Enter Code")
	problem_id = forms.ChoiceField(problems)
	language = forms.ChoiceField([['py','Python 3'],['cpp','C++']])
