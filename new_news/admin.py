from django.contrib import admin
from .models import News, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdminModel(admin.ModelAdmin):
    search_fields = ['id', 'category_name']
    list_filter = ['created_at']
    list_display = ['id', 'category_name', 'created_at']
    ordering = ['-id']

@admin.register(News)
class NewsAdminModel(admin.ModelAdmin):
    search_fields = ['id', 'news_title', 'news_category']
    list_filter = ['created_at']
    list_display = ['id', 'news_title', 'news_category', 'created_at']
    ordering = ['-id']