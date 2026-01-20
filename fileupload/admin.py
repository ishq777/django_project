from django.contrib import admin
from .models import FileUpload

@admin.register(FileUpload)

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'date']
