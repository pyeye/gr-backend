from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Event, Artist, Showman, EventArtistRel


class EventArtistInline(admin.TabularInline):
    model = EventArtistRel
    extra = 2


class EventAdmin(admin.ModelAdmin):
    inlines = (EventArtistInline,)

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }



    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    date_format.admin_order_field = 'date'
    date_format.short_description = 'Дата'

    list_display = ('name', 'date_format')
    filter_horizontal = ('showmen',)
    list_filter = ['date']
    #list_editable = ['is_special']
    search_fields = ['name']
    date_hierarchy = 'date'


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'style')
    list_filter = ['style']
    exclude = ('bio',)
    #list_editable = ['is_special']
    search_fields = ['name']


class ShowmanAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Showman, ShowmanAdmin)
