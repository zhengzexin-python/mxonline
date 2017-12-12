import xadmin
from users.models import EmailVerifyRecord, Banner
from xadmin import views


@xadmin.sites.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


@xadmin.sites.register(Banner)
class BannerAdmin:
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting:
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线教育网'
    menu_style = 'accordion'
