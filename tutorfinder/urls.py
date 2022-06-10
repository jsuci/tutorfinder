from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.core.views import frontpage, dashboard, profile
from apps.api.views import CustomUserList, CustomUserDetail


urlpatterns = [
    path('api/v1/user-list/', CustomUserList.as_view(), name='user_list'),
    path('api/v1/user-detail/<str:pk>/', CustomUserDetail.as_view(), name='user_detail'),
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', frontpage, name='frontpage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
