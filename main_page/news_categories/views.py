from django.shortcuts import render, redirect, get_object_or_404
from .models import News, NewsCategory, About


def index(request):
    if request.user.is_authenticated:
        latest_news = News.objects.order_by('-created_at')[:10]
        context = {'latest_news': latest_news}
        return render(request, 'index.html', context)
    return redirect('about')


def categories(request):
    categories = NewsCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)


def category_news(request, category_id):
    category = get_object_or_404(NewsCategory, id=category_id)
    news = News.objects.filter(news_category=category)
    return render(request, 'category_news.html', {'category': category, 'news': news})


def about(request):
    if request.user.is_authenticated:
        owners = About.objects.all()
        context = {'owners': owners}
        return render(request, 'about.html', context)
    else:
        return redirect('login')


def contacts(request):
    return render(request, 'contacts.html')


def news_detail(request, news_id):
    news = News.objects.filter(id=news_id)
    context = {'news': news}
    return render(request, 'news_detail.html', context)
