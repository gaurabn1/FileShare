from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']