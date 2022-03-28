from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list-feedback/', views.listFeedback, name='list-feedback')
]