from django.db import models

# Create your models here.
class Article(models.Model):
    DEVELOPMENT = "dv" # 대문자는 변하지 않음을 의미함
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    contents = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return "{}에 댓글 : {}".format(self.article.title, self.contents)

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
