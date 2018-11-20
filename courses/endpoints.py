from django.urls import include, path
from rest_framework import routers

from .api import CourseViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]

