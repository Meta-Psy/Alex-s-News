from django.contrib import admin
from .models import News, NewsCategory, About


@admin.register(News)
class NewsAdminModel(admin.ModelAdmin):
    search_fields = ['news_name', 'news_short_description', 'created_at']
    list_filter = ['created_at', ]
    list_display = ['id', 'news_name', 'news_short_description', 'created_at']
    ordering = ['-id']


@admin.register(NewsCategory)
class NewsCategoryAdminModel(admin.ModelAdmin):
    search_fields = ['category_name', 'category_description', 'created_at']
    list_filter = ['created_at']
    list_display = ['category_name', 'category_description', 'created_at']
    ordering = ['-id']


@admin.register(About)
class AboutAdminModel(admin.ModelAdmin):
    search_fields = ['about_name', 'about_descr', 'created_at']
    list_filter = ['created_at']
    list_display = ['about_name', 'about_descr', 'created_at']
    ordering = ['-id']
