from django.db import models


class NewsSite(models.Model):
    """ニュースサイトモデル"""
    class Meta:
        db_table = 'news_site'

    name = models.CharField(max_length=255)
    base_url = models.CharField(max_length=255)
    is_code_exist = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):
    """カテゴリモデル"""
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NewsSiteCategory(models.Model):
    """ニュースサイトとカテゴリを紐付けるモデル"""
    class Meta:
        db_table = 'news_site_category'

    news_site = models.ForeignKey(NewsSite, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Article(models.Model):
    """記事モデル"""
    class Meta:
        db_table = 'article'

    news_site = models.ForeignKey(NewsSite, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    category_id = models.IntegerField()

    def __str__(self):
        return self.title
