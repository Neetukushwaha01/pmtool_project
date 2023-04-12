from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView

from rest_framework import generics, status

from rest_framework.response import Response


class ProjectView( APIView ):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        context = {}
        posts = ProjectDetails.objects.filter()
        posts_list = ProjectDetailsSerializer( posts, many=True, context={"request": request} )
        context['data'] = posts_list.data
        return Response( context, status=status.HTTP_200_OK )

    def post(self, request):
        context = {}
        user = request.user
        data = request.data
        print( "data ", data )
        # try:
        project = ProjectDetails.objects.create(
            user=user,
            name=data['name'],
            start_date=data['start_date'],
            due_date=data['due_date'],
            request_type=data['request_type'],
            description=data['description'],
            loom_links=data['loom_links'],
            no_of_pages=data['no_of_pages'],
        )

        # for i in list(data['attachment']):
        ProjectAttachment.objects.create( project=project, attachment=data['attachment'] )

        serializer = ProjectDetailsSerializer( project, many=False, context={"request": request} )
        context['data'] = serializer.data

        return Response( context, status=status.HTTP_201_CREATED )
        # except:
        #     return Response(context,status = status.HTTP_400_BAD_REQUEST)


# this code for viedo aad  start
class VideoApi( APIView ):

    def post(self, request):
        serializer = ViedoProjectSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


def get(self, request, format=None):
    context = {}
    video = ViedoProject.objects.filter()
    video_list = ViedoProjectSerializer( video, many=True, context={"request": request} )
    context['data'] = video_list.data
    return Response( context, status=status.HTTP_200_OK )

    # this code for viedo aad  end
