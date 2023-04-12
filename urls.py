from django.urls import path,include
from .views import *

urlpatterns = [
    path('project/', ProjectView.as_view(), name='project'),
    path('videos/', VideoApi.as_view(),name="Video"),#this is a viedo urls


]
