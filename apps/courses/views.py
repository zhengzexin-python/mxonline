from django.http import HttpResponse
from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin


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


class CourseDetailView(View):
    """
    课程详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        # 增加点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []

        return render(request, 'course-detail.html', {
            'course': course,
            'relate_courses': relate_courses,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org
        })


class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_course_resources = CourseResource.objects.filter(course=course)
        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [user_course.course.id for user_course in all_user_courses]
        relate_course = Course.objects.filter(id__in=course_ids).order_by('-click_nums')[:5]
        current_page = 'info'
        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': all_course_resources,
            'current_page': current_page,
            'relate_course': relate_course
        })


class CommentsView(LoginRequiredMixin, View):
    """
    课程评论
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        all_course_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course)
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [user_course.course.id for user_course in all_user_courses]
        relate_course = Course.objects.filter(id__in=course_ids).order_by('-click_nums')[:5]
        current_page = 'comments'

        return render(request, 'course-comment.html', {
            'course': course,
            'course_resources': all_course_resources,
            'all_comments': all_comments,
            'current_page': current_page,
            'relate_course': relate_course
        })


class AddCommentView(View):
    """
    添加评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')
        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if int(course_id) > 0 and comments:
            course_comments = CourseComments()
            course_comments.course = Course.objects.get(id=int(course_id))
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加失败"}', content_type='application/json')
