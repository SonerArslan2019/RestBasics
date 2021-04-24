from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    authot = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'article'
    #     verbose_name = 'Article'
    #     verbose_name_plural = 'Article'

    def __str__(self):
        return self.title
