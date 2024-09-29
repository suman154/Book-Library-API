from django.contrib import admin
from .models import Departure
# Register your models here.

from django.contrib import admin
from .models import Departure


class DepartureInline(admin.TabularInline):
    model = Departure
    extra = 1 


@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    list_display = ('departure', 'start_date', 'end_date', 'language', 'price')
    inlines = [DepartureInline]
