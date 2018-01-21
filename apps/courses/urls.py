from django.conf.urls import url

from .views import CourseListView

app_name = 'course'

urlpatterns = [
   url(r'^list/$', CourseListView.as_view(), name='list')
]