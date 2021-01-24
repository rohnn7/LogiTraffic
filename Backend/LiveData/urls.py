from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from LiveData.views import (LiveDataDetailAPIView,
                            LiveDataListAPIView,
                            LiveDataUpdateAPIView,
                            LiveDataDeleteAPIView)



app_name = 'LiveData'
urlpatterns = [
    url(r'edit/(?P<pk>\d+)$', LiveDataUpdateAPIView.as_view(), name='update'),
    url(r'detail/(?P<pk>\d+)$', LiveDataDetailAPIView.as_view(), name='detail'),
    url(r'delete/(?P<pk>\d+)$', LiveDataDeleteAPIView.as_view(), name='delete'),
    url(r'list/$', LiveDataListAPIView.as_view(), name='list'),   
]


