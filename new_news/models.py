from django.db import models

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name='Категория новостей'
        verbose_name_plural='Категории новостей'

class News(models.Model):
    news_title = models.CharField(max_length=150)
    news_text = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
