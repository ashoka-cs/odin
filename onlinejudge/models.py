from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime




# Create your models here.
class Contest(models.Model):
    contest_title=models.CharField(max_length=200)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    contest_description=models.TextField()

    def __str__(self):
        return str(self.id) + " : " + self.contest_title
    
class Problem(models.Model):
    problem_id = models.CharField(max_length=30, primary_key=True)
    problem_title = models.CharField(max_length=30)
    problem_statement = models.TextField()
    timelimit = models.IntegerField(default=1)
    memlimit = models.IntegerField(default=256000)
    no_of_test_cases= models.IntegerField(default=1)
    contest=models.ForeignKey(Contest, on_delete= models.CASCADE)
    problem_score=models.IntegerField(default=1)


    def __str__(self):
        return str(self.problem_id) + " : " + self.problem_title

class Submission(models.Model):

    problem = models.ForeignKey(Problem, on_delete= models.CASCADE)
    time_of_submission = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    languages = [['py','Python 3'],['cpp','C++']]
    language = models.CharField(max_length = 20, default = 'py', choices = languages)
    verdict=models.CharField(max_length=50)

    def __str__(self):
        return "Submission number: "+ str(self.id)

class LeaderboardEntry(models.Model): # For one user, not for one rank. 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    score = models.IntegerField() # Simply ranks by score currently. 
#    last_submission_time = models.DateTimeField(blank=True, null=True)


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['problem','code','language']



