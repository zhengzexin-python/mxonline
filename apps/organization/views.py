from django.shortcuts import render
# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse
from pure_pagination import Paginator, PageNotAnInteger

from organization.forms import UserAskForm
from .models import CourseOrg, City


class OrgView(View):
    """
    课程机构列表功能
    """

    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = CourseOrg.objects.all().order_by('-click_nums')[:3]

        # 类别过滤
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 城市过滤
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=city_id)

        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-student_nums')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        org_count = all_orgs.count()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'orgs': orgs,
            'all_citys': all_citys,
            'org_count': org_count,
            'category': category,
            'city_id': city_id,
            'sort': sort,
            'hot_orgs': hot_orgs
        })


class AddUserAskView(View):
    """
    用户添加咨询

    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加出错"}', content_type='application/json')
