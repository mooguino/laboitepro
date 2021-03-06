from django.contrib import admin

from .models import AppTime

class AppTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('time', 'date', 'created_date', 'last_activity')

    list_display = ('boite', 'enabled', 'tz', 'created_date', 'last_activity')

admin.site.register(AppTime, AppTimeAdmin)
