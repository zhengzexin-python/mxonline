from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentView

app_name = 'course'

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='info'),
    url(r'^comments/(?P<course_id>\d+)/$', CommentsView.as_view(), name='comment'),
    url(r'add_comments/$', AddCommentView.as_view(), name='add_comments')
]
