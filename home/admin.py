from django.contrib import admin
from django.utils.html import format_html
from . import models


class IncidentAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src={obj.image} width='128' height='128' />")

    def fullImg(self, obj):
        return format_html(f"<img src={obj.image} width='512' height='512' />")

    def location_info(self, obj):
        if obj.location == None:
            return ''
        
        if obj.location.startswith("[::GPS::]"):
            loc = obj.location[9:]
            loc = loc.split('|')
            return format_html(f"<a href='https://www.google.com/maps/@{loc[0]},{loc[1]},18z' target='_blank'>View Location</a>")
        return obj.location

    list_display = ['thumbnail', 'title',
                    'location_info', 'type', 'status', 'date_time']
    fields = ['fullImg', 'title', 'date_time',
              'location_info', 'type', 'details', 'status']
    readonly_fields = ['fullImg', 'location_info', 'date_time']


admin.site.register(models.IncidentModel, IncidentAdmin)
