from django.conf.urls import url
from django.views.generic import TemplateView
from Demo1 import views as demo1_views

urlpatterns = [
    url(r'^$', demo1_views.index, name='index'),
    url(r'^account/signup', demo1_views.signup, name='signup'),
    url(r'^account/signin', demo1_views.signin, name='signin'),
    url(r'^user', demo1_views.user, name='user'),
    url(r'^account/reset_password/', demo1_views.reset_password, name='reset_password'),
]
