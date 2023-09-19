import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','send_mail.settings')
app=Celery('send_mail')
app.config_from_object('django.conf:settings', namespace="CELERY")
from celery.schedules import solar

# app.conf.beat_schedule={
#     'send-mail-at-3 every-day':{
#         'task':'send_mail_app.tasks.sending_mail',
#         # 'task':'send_mail_app.tasks.send_mail_function',
#         # 'schedule':crontab(minute='*/2'),                    
        
#         'schedule':crontab(hour=18, minute=1),
         
#         # 'schedule': solar('sunset', -37.81753, 144.96715),
#         # "args": ["EmailMessage"],
#         # 'args' : ('4'),
        
#         #second method
#         'args': ((('Subject 1', 'Message 1', 'raiyanar0@gmail.com', ['raiyyanabdurrehman@gmail.com']),
#                   ('Subject 2', 'Message 2', 'raiyanar0@gmail.com', ['raiyyanabdurrehman@gmail.com'])),)        
    
#     }
# }


# app.conf.beat_schedule={
#     'send-mail-at-3 every-day':{
#         'task':'send_mail_app.tasks.send_mail_with_attachments',
#         'schedule':crontab(hour=18, minute=1),
#         'args':((('subject_','Message1',['raiyanar0@gmail.com'],'f"{settings.BASE_DIR}/mail.xlsx"')),)
#     }
# }

# from send_mail_app.views import mailing

# app.conf.beat_schedule = {
#     'send-mail-at-3 every-day': {
#         'task': 'send_mail_app.tasks.send_mail_with_attachments',
#         'schedule': crontab(hour=16, minute=1),
#         'args': ('subject_', 'Message1', ['raiyanar0@gmail.com'], f"{settings.BASE_DIR}/static/target.xlsx")
#     }
# }

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
