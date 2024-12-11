from django.db import models


class NewsCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    category_image = models.FileField(upload_to='news_images')
    category_news_num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'


class News(models.Model):
    news_name = models.CharField(max_length=100)
    news_short_description = models.TextField()
    news_full_description = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, default=1)
    news_image = models.FileField(upload_to='news_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class About(models.Model):
    about_name = models.CharField(max_length=100)
    about_descr = models.TextField()
    about_image = models.FileField(upload_to='author_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_name

    class Meta:
        verbose_name = 'Владелец сайта'
        verbose_name_plural = 'Владельцы сайта'
