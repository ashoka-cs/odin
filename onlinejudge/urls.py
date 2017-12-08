from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    #url(r'^signup/$', views.signup, name="signup"),
    #url(r'^login/$', views.login, name="login"),

    url(r'^$', auth_views.login, name="login"),
    url(r'^problemset/$', views.problemset, name="problemset"),
    url(r'^submissions/$', views.submissions, name = "submissions"),
    url(r'^logout/$', auth_views.logout , {'next_page': 'login'} , name="logout"),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^contestlist/$', views.contestlist, name = 'contestlist'),

    url(r'^contest/(?P<contest_pk>\d+)/$', views.contest_detail, name = 'contest_detail'),
    url(r'^problem/(?P<problem_pk>\d+)/$', views.problem_detail, name = 'problem_detail'),

]
