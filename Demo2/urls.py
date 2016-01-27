from django.conf.urls import url
from Demo2 import views as demo2_views

urlpatterns = [
    url(r'^signup/$', demo2_views.signup.as_view(), name='signup2'),
    url(r'^user/$', demo2_views.user.as_view(), name='user2'),
    url(r'^reset_password/$', demo2_views.reset_password.as_view(), name='reset_password2'),
]
