from django.urls import path

from quick.views import TwitterApi

urlpatterns = [
    path('twitter/<id>/', TwitterApi.as_view(), name = 'twitter'), 
]