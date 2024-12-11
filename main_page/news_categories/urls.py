from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_news, name='category_news'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news_detail/<int:news_id>/', views.news_detail, name='news_detail'),
]
