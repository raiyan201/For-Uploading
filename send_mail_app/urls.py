from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('', views.send_mail_to_gmail,name="home"),
    path('send-email', views.send_email,name="send-email"),
    path('send-attachment',views.send_xlsx,name="send-attachment"),
    path('excel-export',views.export_data_xls,name="excel-export"),
    path('register/',views.register,name="register"),
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout,name="logout"),
    path('download',views.download_data,name="download-data"),
    # path('attach-file',views.attach_file,name='attach-file'),
    path('attach-file',views.attach_file1,name='attach-file'),
    path('mailing',views.mailing,name='mailing'),
    path('file-convert',views.file_convert,name='file-convert'),
    # path('<task_id>',views.checkstatus,name="check-status"),
    path('mailing-all',views.mailing_all,name='mailing_all'),    
    path('email-history',views.email_history,name='email-history'),

]
