from django.conf.urls import url

from organization.views import OrgView

app_name = 'org'

urlpatterns = [
    url(r'org_list', OrgView.as_view(), name='org_list')
]
