from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    #url(r'^signup/$', views.signup, name="signup"),
    #url(r'^login/$', views.login, name="login"),
    # TODO make strings more consistent, use only 'string', or "string", but not both.
    path('', auth_views.login, name="login"),
    path('problemset/', views.problemset, name="problemset"),
    path('submissions/', views.submissions, name = "submissions"),
    path('logout/', auth_views.logout , {'next_page': 'login'} , name="logout"),
    path('signup/', views.signup, name='signup'),
    path('my_submissions/', views.my_submissions, name="my_submissions"),
    path('contestlist/', views.contestlist, name = 'contestlist'),
    path('leaderboard/<int:contest_pk>', views.leaderboard, name = 'leaderboard'),
    path('contest/<int:contest_pk>', views.contest_detail, name = 'contest_detail'),
    path('problem/<int:problem_pk>', views.problem_detail, name = 'problem_detail'),
]
