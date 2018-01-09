from django.conf.urls import url

from organization.views import OrgView, AddUserAskView

app_name = 'org'

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]
