from django.contrib import admin
from my.models import studentdata
# Register your models here.

@admin.register(studentdata)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email']
