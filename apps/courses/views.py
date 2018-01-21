from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Course


class CourseListView(View):
    """
    课程列表页
    """

    def get(self, request):
        courses = Course.objects.all().order_by('-add_time')
        hot_courses = courses.order_by('-click_nums')[:3]
        sort = request.GET.get('sort', '')
        if sort == 'hot':
            courses = courses.order_by('-click_nums')
        elif sort == 'students':
            courses = courses.order_by('-students')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(courses, 3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'courses': courses,
            'sort': sort,
            'hot_courses': hot_courses
        })
