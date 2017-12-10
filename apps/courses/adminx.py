import xadmin
from .models import Course, Lesson, Video, CourseResource


@xadmin.sites.register(Course)
class CourseAdmin:
    list_display = (
        'name', 'degree', 'learn_time', 'students', 'fav_nums', 'click_nums',
        'add_time',
    )
    search_fields = ('name', 'desc', 'detail', 'degree',)
    list_filter = (
        'name', 'desc', 'detail', 'degree', 'learn_time', 'students',
        'fav_nums', 'click_nums', 'add_time',
    )


@xadmin.sites.register(Lesson)
class LessonAdmin:
    list_display = ('course', 'name', 'add_time',)
    search_fields = ('course__name', 'name',)
    list_filter = ('course__name', 'name', 'add_time',)


@xadmin.sites.register(Video)
class VideoAdmin:
    list_display = ('lesson', 'name', 'add_time',)
    search_fields = ('lesson__name', 'name',)
    list_filter = ('lesson__name', 'name', 'add_time',)


@xadmin.sites.register(CourseResource)
class CourseResourceAdmin:
    list_display = ('course', 'name', 'download', 'add_time')
    search_fields = ('course__name', 'name', 'download')
    list_filter = ('course__name', 'name', 'download', 'add_time')
