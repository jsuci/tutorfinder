from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.core.views import frontpage, dashboard
from apps.api.views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', frontpage, name='frontpage'),
    path('dashboard/', dashboard, name='dashboard'),
]
