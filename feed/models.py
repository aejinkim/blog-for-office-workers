from django.db import models

# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv" # 대문자는 변하지 않음을 의미함
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )#tuple

    title = models.CharField(max_length=200)
    contents = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    #Article에서 타이틀이 보이게 함 (클래스 안에 함수 쓰려면 self)
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name = "article_comments",
        on_delete=models.CASCADE
    )
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}에 댓글 : {}".format(self.article.title, self.contents)

# class HashTag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
