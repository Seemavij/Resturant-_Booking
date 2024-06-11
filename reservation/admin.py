from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_filter = ('time',)
    search_fields = ['name', 'date']
    list_display = ['name', 'date']
