from django.contrib import admin

from.models import SourceFile


class SourceFileAdmin(admin.ModelAdmin):
    list_display = ['path', 'file_name', 'version']
    list_display_links = ['file_name', ]
    list_filter = ['version', ]

admin.site.register(SourceFile, SourceFileAdmin)
