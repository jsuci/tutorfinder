from django.contrib import admin
from django.urls import path, include

from apps.core.views import homepage, dashboard, profile, search
from apps.api.views import CustomUserList, CustomUserDetail, TutorList


urlpatterns = [
    path('api/v1/user-list/', CustomUserList.as_view(), name='user_list'),
    path('api/v1/user-list/tutors/', TutorList.as_view(), name='tutor_list'),
    path('api/v1/user-detail/<str:pk>/',
         CustomUserDetail.as_view(), name='user_detail'),
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('search/', search, name='search')
]

