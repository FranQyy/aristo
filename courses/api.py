from rest_framework import viewsets, permissions

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CourseSerializer