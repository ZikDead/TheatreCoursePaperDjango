from django.contrib import admin
from .models import EventList, Hall, Performance


@admin.register(EventList)
class EventListAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(Performance)
class ProgramAdmin(admin.ModelAdmin):
    pass




