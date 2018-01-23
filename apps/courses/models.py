from django.db import models
from django.utils import datetime_safe

from organization.models import CourseOrg


# Create your models here.


class Course(models.Model):
    """
    课程
    """
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(
        choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')),
        max_length=2,
        verbose_name='难度')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(max_length=20, verbose_name='课程类别', default='')
    tag = models.CharField(max_length=20, verbose_name='课程标签', default='')
    add_time = models.DateTimeField(
        default=datetime_safe.datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        """
        获取章节数
        :return:
        """
        return self.lesson_set.all().count()

    def get_learn_users(self):
        """
        获取学习用户
        :return:
        """
        return self.usercourse_set.all()[:5]

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    """
    章节
    """
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(
        default=datetime_safe.datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    """
    视频
    """
    lesson = models.ForeignKey(Lesson, verbose_name='章节名')
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(
        default=datetime_safe.datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    """
    课程资源
    """
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(
        upload_to='course/resource/%Y/%m', verbose_name='资源位置')
    add_time = models.DateTimeField(
        default=datetime_safe.datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
