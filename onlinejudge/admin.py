from django.contrib import admin
from .models import Problem, Submission, Contest, LeaderboardEntry

# Register your models here.
admin.site.register(LeaderboardEntry)
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Contest)
