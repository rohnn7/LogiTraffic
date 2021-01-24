from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from User.views import (UserExtendedListAPIView,
                        UserExtendedRetrieveAPIView,
                        UserExtendedUpdateAPIView,
                        UserExtendedDeleteAPIView,
                        UserExtendedCreateAPIView,
                        UserCreateAPIView,
                        UserLoginAPIView)

app_name = 'User'
urlpatterns = [
    url(r'list/$', UserExtendedListAPIView.as_view(), name='list'),
    url(r'detail/(?P<pk>\d+)$', UserExtendedRetrieveAPIView.as_view(), name='detail'),
    url(r'edit/(?P<pk>\d+)$', UserExtendedUpdateAPIView.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)$', UserExtendedDeleteAPIView.as_view(), name='delete'),
    url(r'create/$', UserExtendedCreateAPIView.as_view(), name='create'),
    url(r'register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'login/$', UserLoginAPIView.as_view(), name='login'),
]

