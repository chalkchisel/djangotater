from django.contrib import admin

from .models import Version, SourceFile


class VersionAdmin(admin.ModelAdmin):
    list_display = ['name', 'identifier']


class SourceFileAdmin(admin.ModelAdmin):
    list_display = ['path', 'file_name', 'version']
    list_display_links = ['file_name', ]
    list_filter = ['version', ]

admin.site.register(Version, VersionAdmin)
admin.site.register(SourceFile, SourceFileAdmin)
