from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Course


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin):
    model = Course


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'


# TWORZENIE WIDOKóW Z DOMIESZKAMI
class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'courses/home.html')


def login(request):
    return render(request, 'courses/login.html')
