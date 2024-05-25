from django.contrib import admin
from .models import Menu, Category


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ['category', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
