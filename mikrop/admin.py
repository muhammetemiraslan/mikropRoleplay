from django.contrib import admin
from .models import Category, Character, CharacterDetail

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') 
    search_fields = ('name',)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_home')
    search_fields = ('name',)
    list_filter = ('is_home', 'categories')
    filter_horizontal = ('categories',)
    list_display = ('name', 'is_home', 'image_preview')
    readonly_fields = ('image_preview',)

class CharacterDetailAdmin(admin.ModelAdmin):
    list_display = ('character', 'title', 'years')
    search_fields = ('character__name', 'title')
    raw_id_fields = ('character',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterDetail, CharacterDetailAdmin)