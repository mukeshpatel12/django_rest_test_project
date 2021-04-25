from django.contrib import admin
from.models import Holiday

"""
Register Holiday model for Admin section
"""
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'type', 'date', 'user')
    search_fields = ('name', 'type', 'country', )
    list_filter = ('name', 'type', 'country', )

admin.site.register(Holiday, HolidayAdmin)