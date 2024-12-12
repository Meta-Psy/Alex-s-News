from django.urls import path, re_path
from . import views
from user.views import register_view, login_view, logout_view

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_news, name='category_news'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news_detail/<int:news_id>/', views.news_detail, name='news_detail'),
    path('registration/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]