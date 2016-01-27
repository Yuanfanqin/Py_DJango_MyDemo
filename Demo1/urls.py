from django.conf.urls import url
from django.views.generic import TemplateView
from Demo1 import views as demo1_views
from rest_framework.authtoken import views as rf_views

urlpatterns = [
    url(r'^page_signup/$', demo1_views.page_signup, name='page_signup'),
    url(r'^page_signin/$', demo1_views.page_signin, name='page_signin'),
    url(r'^page_reset_password/$', demo1_views.page_reset_password, name='page_reset_password'),
    url(r'^account/signup/', demo1_views.signup, name='signup'),
    url(r'^account/signin/', demo1_views.signin, name='signin'),
    url(r'^user/', demo1_views.user, name='user'),
    url(r'^account/reset_password/', demo1_views.reset_password, name='reset_password'),
    url(r'^api-token-auth/', rf_views.obtain_auth_token)
]
