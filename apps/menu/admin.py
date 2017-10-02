from django.contrib import admin

from .models import Menu, Price, Category, Group


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1
    exclude = ('extra',)


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

    def get_category(self, obj):
        return obj.category.name
    get_category.short_description = 'Категория'
    get_category.admin_order_field = 'category__name'

    list_display = ('name', 'get_category', 'is_active', 'is_lunch')
    list_filter = ['is_active', 'category__name', 'is_lunch']
    search_fields = ['name']

    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    search_fields = ['name']
    exclude = ('extra',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)

