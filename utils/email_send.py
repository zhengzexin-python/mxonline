"""邮件发送工具类"""
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM


def random_str(random_length=8):
    """
    生成随机字符串
    Args:
        random_length(int):随机字符串长度
    Returns:
        string(str): 返回的随机字符串
    """
    string = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        string += chars[random.randint(0, length)]
    return string


def send_email(email, send_type='register'):
    """
    发送邮件
    Args:
        email(str):目标邮箱
        send_type(str): 发送类型
    """
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        email_body = '请点击下面链接激活您的账号:http://127.0.0.1:8000/active/{0}'.format(code)
        send_status =send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            pass
