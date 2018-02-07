from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django_ace import AceWidget
import datetime




# Create your models here.
class Contest(models.Model):
    contest_title=models.CharField(max_length=200) # TODO switch contest_title to simply title (and same for contest_description). 
    start_time=models.DateTimeField() # TODO (contd.) Writing contest.contest_title is stupid because of the repeated constant, but I have to find all places where that is used. 
    end_time=models.DateTimeField()
    contest_description=models.TextField()
    visible = models.BooleanField(default=True)
    def is_running(self):
        current_time=datetime.datetime.now(datetime.timezone.utc)
        print(current_time)
        if current_time > self.start_time and current_time < self.end_time:
            return True
        return False

    def __str__(self):
        return str(self.id) + " : " + self.contest_title

    def save(self, *args, **kwargs):
        super(Contest, self).save(*args, **kwargs)
        if not self.is_running():
            leaderboardentries = LeaderboardEntry.objects.filter(contest=self).order_by('-score')
            users = User.objects.all()
            for user in users:
                 LeaderboardEntry.objects.create(user_id=user.id,contest_id=self.id)
                 print(user)
        

        
    
class Problem(models.Model):

    contest=models.ForeignKey(Contest, on_delete= models.CASCADE)


    problem_id = models.CharField(max_length=30, primary_key=True)
    problem_title = models.CharField(max_length=30)
    problem_statement = models.TextField()
    timelimit = models.IntegerField(default=1)
    memlimit = models.IntegerField(default=256000)
    no_of_test_cases= models.IntegerField(default=1)
    problem_score=models.IntegerField(default=1)

    def __str__(self):
        return str(self.problem_id) + " : " + self.problem_title

class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete= models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_submission = models.DateTimeField(auto_now=True)
    code = models.TextField()
    languages = [['py','Python 3'],['cpp','C++'],['c','C'],['java','Java']]
    language = models.CharField(max_length = 20, default = 'py', choices = languages)
    verdict=models.CharField(max_length=50)

    def __str__(self):
        return str(self.problem) + " | " + str(self.contest) + " | " + str(self.user) + " | " + str(self.verdict)

class LeaderboardEntry(models.Model): # For one user, not for one rank - therefore think of this as the relation between User
    # and contest, each User has one LeaderboardEntry in each Contest.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    score = models.IntegerField(default=0) # Simply ranks by score currently.
    last_submission_time = models.DateTimeField(null=True)
    def on_correct_answer(self, problem, time_of_submission): # problem is an instance of model Problem
        # if there are more than 1 accepted problem submission for this user and this contest then we don't need to add to score.
        submission = Submission.objects.filter(contest_id=self.contest_id,user_id=self.user_id,problem_id=problem,verdict="Correct Answer")
        print(submission)
        if(len(submission)==1): # i.e. if the current accepted submission is the ONLY accepted submission so far, we can increase score.
            self.score+=1
            self.last_submission_time= time_of_submission
        self.save()

    def __str__(self):
        return "User " + str(self.user) + " is registered for Contest #" + str(self.contest)
#    last_submission_time = models.DateTimeField(blank=True, null=True)


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['problem','code','language']
        def __init__(self, *args, **kwargs):
            super(SubmissionForm, self).__init__(*args, **kwargs)
            self.fields["code"].widget = forms.CharField(widget=AceWidget(mode='python'))

