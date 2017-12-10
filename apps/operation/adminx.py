import xadmin

from .models import UserAsk, UserCourse, UserFavorite, UserMessage


@xadmin.sites.register(UserAsk)
class UserAskAdmin:
    list_display = ('name', 'mobile', 'course_name', 'add_time',)
    search_fields = ('name', 'mobile', 'course_name',)
    list_filter = ('name', 'mobile', 'course_name', 'add_time',)


@xadmin.sites.register(UserCourse)
class UserCourseAdmin:
    list_display = ('user', 'course', 'add_time',)
    search_fields = ('user__username', 'course__name',)
    list_filter = ('user__username', 'course__name', 'add_time',)


@xadmin.sites.register(UserFavorite)
class UserFavoriteAdmin:
    list_display = ('user', 'fav_id', 'fav_type', 'add_time',)
    search_fields = ('user__username', 'fav_id', 'fav_type',)
    list_filter = ('user__username', 'fav_id', 'fav_type', 'add_time',)


@xadmin.sites.register(UserMessage)
class UserMessageAdmin:
    list_display = ('user', 'message', 'has_read', 'add_time',)
    search_fields = ('user__username', 'message', )
    list_filter = ('user__username', 'message', 'has_read', 'add_time',)

