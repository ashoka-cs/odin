from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'', auth_views.login, name="login"),
    #url(r'^login/$', views.login, name="login"),
    url(r'^problemset/$', views.problemset, name="problemset")
   
]
