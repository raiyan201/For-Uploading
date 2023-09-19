from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from send_mail import settings
from django.utils import timezone
from datetime import timedelta
from django.core.mail import EmailMessage
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

# @shared_task(bind=True)
# def send_mail_function(self):
#     users=get_user_model().objects.all()
    
#     for user in users:
#         print("mailing")
#         mail_subject="Periodic Task"
#         message="Happy Teachers day to everyone"        
#         to_email=user.email
#         print(to_email)
        
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=False
#         )
        
#     return "Done"


# def send_mail_with_atachments(subject,message,recipient_list,file_path):
#     mail=EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipient_list)
#     mail.attach_file(file_path)
#     mail.send()
    
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage

#first-method
# @shared_task(bind=True)
# def sending_mail(self,**kwargs):
    
#     email1=(kwargs["subject"],kwargs["message"],kwargs["from"],[kwargs["to"]])
#     email2=(kwargs["subject"],kwargs["message"],kwargs["from"],[kwargs["to"]])    
#     messages=(email1,email2)
#     send_mass_mail(messages,fail_silently=False)

    
@shared_task
def sending_mail(email_messages):
    send_mass_mail(email_messages, fail_silently=False)

# from send_mail_app.views.mailing import year,month,date,hour,minutes
# # from datetime import year

from datetime import datetime
# schedule_time=datetime(int(year),
# int(month),int(date),
# int(hour),int(minutes))                                       
                                              
                       
# @shared_task
# def send_mail_with_attachments(subject, message, recipient_list, file_path, year, month, date, hour, minutes):
#     schedule_time = datetime(int(year), int(month), int(date), int(hour), int(minutes))
#     mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
#     mail.attach_file(file_path)
#     mail.send(fail_silently=False)

@shared_task
def send_mail_with_attachments(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    mail.send(fail_silently=False)



from docx2pdf import convert
from time import sleep
@shared_task
def doc_to_pdf(files):    
    sleep(10)
    convert('static/' + files)
    return None

