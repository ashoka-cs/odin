from django.db import models

# Create your models here.
class Problem(models.Model):
    problem_id = models.CharField(max_length=30, primary_key=True)
    problem_title = models.CharField(max_length=30)
    problem_statement = models.TextField()
    def __str__(self):
        return str(self.problem_id) + " : " + self.problem_statement[0:10]
