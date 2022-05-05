from django.urls import path, include
from tutor import views


urlpatterns = [
    path('list-tutors/', views.AllTutorsList.as_view()),
]