from django.shortcuts import render

from .serializers import TutorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Tutor
from .serializers import TutorSerializer


class AllTutorsList(APIView):
    def get(self, request, format=None):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)

        return Response(serializer.data)
