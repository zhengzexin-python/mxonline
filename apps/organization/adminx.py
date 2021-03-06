import xadmin
from .models import City, CourseOrg, Teacher


@xadmin.sites.register(City)
class CityAdmin:
    list_display = ('name', 'desc', 'add_time',)
    search_fields = ('name', 'desc',)
    list_filter = ('name', 'desc', 'add_time',)


@xadmin.sites.register(CourseOrg)
class CourseOrgAdmin:
    list_display = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time',)
    search_fields = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name',)
    list_filter = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time',)


@xadmin.sites.register(Teacher)
class TeacherAdmin:
    list_display = (
        'org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time',)
    search_fields = (
        'org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',)
    list_filter = (
        'org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time',)
