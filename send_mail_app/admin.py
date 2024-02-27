from django.contrib import admin
from .models import Employee,Customer,EmailHistory
# Register your models here.
# from import_export.admin import ImportExportModelAdmin
# admin.site.register(Employee)

# @admin.register(Employee)
# class detail(ImportExportModelAdmin):
#     pass

admin.site.register(Customer)
admin.site.register(EmailHistory)
