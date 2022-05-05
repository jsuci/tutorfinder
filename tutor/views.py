from django.shortcuts import render

from .serializers import TutorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Tutor, Category
from .serializers import TutorSerializer, CategorySerializer


class AllTutorsList(APIView):
    def get(self, request, format=None):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)

        return Response(serializer.data)

class AllCategoriesList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)
