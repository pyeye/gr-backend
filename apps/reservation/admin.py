from django.contrib import admin

from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):

    def time_start_format(self, obj):
        return obj.time_start.strftime("%H:%M")
    time_start_format.admin_order_field = 'time_start'
    time_start_format.short_description = 'C'

    def time_end_format(self, obj):
        return obj.time_end.strftime("%H:%M")

    time_end_format.admin_order_field = 'time_end'
    time_end_format.short_description = 'До'

    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = (
        'name',
        'sur_name',
        'phone_number',
        'email',
        'date_format',
        'time_start_format',
        'time_end_format',
        'count_people',
    )

    search_fields = ['phone_number', 'phone_number', 'email']

admin.site.register(Reservation, ReservationAdmin)
