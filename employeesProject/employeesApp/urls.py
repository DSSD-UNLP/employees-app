from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view()),
    url(r'^employee/login/(?P<email>.*)/$', views.EmployeeLogin.as_view()),
    url(r'^types/$', views.TypeList.as_view()),
    url(r'^type/(?P<pk>[0-9]+)/$', views.TypeDetail.as_view())
]