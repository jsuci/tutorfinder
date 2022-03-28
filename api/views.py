from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FeedbackSerializer
from .models import Feedback

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list-feedback/',
        'Detail View': '/detail-feedback/<str:pk>',
        'Create': '/create-feedback/',
        'Update': '/update-feedback/',
        'Delete': '/delete-feedback'
    }

    return Response(api_urls)


@api_view(['GET'])
def listFeedback(request):
    listOfFeedback = Feedback.objects.all()
    serializer = FeedbackSerializer(listOfFeedback, many=True)

    return Response(serializer.data)

