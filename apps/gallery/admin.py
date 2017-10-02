from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Image, Album


class ImageInline(admin.TabularInline):
    model = Image
    extra = 10
    exclude = ('extra',)


class AlbumAdmin(ImageCroppingMixin, admin.ModelAdmin):

    def date_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    date_f.admin_order_field = 'created_at'
    date_f.short_description = 'Созданно'

    def event_admin(self, obj):
        return obj.event.name
    event_admin.short_description = 'Событие'
    event_admin.admin_order_field = 'event__name'

    inlines = [ImageInline]
    list_display = ('event_admin', 'date_f')
    date_hierarchy = 'created_at'
    exclude = ('extra',)


class ImageAdmin(admin.ModelAdmin):
    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")

    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    list_display = ('info', 'created_at_f')
    date_hierarchy = 'created_at'


admin.site.register(Album, AlbumAdmin)

