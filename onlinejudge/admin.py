from django.contrib import admin
from .models import Problem, Submission, Contest

# Register your models here.
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Contest)
