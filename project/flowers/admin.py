from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Flower, Types

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descriptions', 'price', 'get_image')
    list_display_links = ('name','descriptions')
    list_filter=('descriptions',)
    search_fields=('name','descriptions')
    list_per_page=2
    ordering=('id',)

    def get_image (self, flower):
        if flower.image:
            return mark_safe(f'<img src="{flower.image.url}" width="75px">')
        else:
            return '😒🙌'
    get_image.short_description='gulning rasmi'



admin.site.register(Flower, FlowerAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_display_links = ('name',)
    list_filter=('color',)
    search_fields=('color','name')
admin.site.register(Types, TypeAdmin)
