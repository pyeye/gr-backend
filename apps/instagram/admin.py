from django.contrib import admin

from .models import Instagram, Category


class InstagramAdmin(admin.ModelAdmin):

    def created_at_f(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")

    created_at_f.admin_order_field = 'created_at'
    created_at_f.short_description = 'Созданно'

    list_display = ('short_code', 'created_at_f')
    #list_editable = ['is_special']
    exclude = ('likes', 'img', 'comments_count', 'extra')
    search_fields = ['short_code']
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Instagram, InstagramAdmin)
admin.site.register(Category, CategoryAdmin)


