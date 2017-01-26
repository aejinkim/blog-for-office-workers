from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Article, Comment, HashTag

# Create your views here.
def index(request):

    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()
    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.objects.filter(hashtag__name=hashtag)


    #####GET & POST
    # POST : 서버에 데이터를 저장 하거나 등 서버에 특정 작업을 요청할 경우 post방식을 씀
    # GET : 사이트를 리프레쉬 하는 전체 동작
        ## ? 뒤에 키와 밸류, & 키와 밸류 등 추가적인 데이터를 같이 보낼 수 있다.
        ## query Dict[]
        ##


    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)

    # category_list = set([
    #     article.get_category_display()
    #     for article in article_list #for문 앞의 구문을 리스트로 만들어 주겠다 (파이썬 구문)
    # ])

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list #for문 앞의 구문을 리스트로 만들어 주겠다 (파이썬 구문)
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, 'index.html', ctx)

def detail(request, article_id):

    article = Article.objects.get(id=article_id)
    # comment_list = Comment.objects.filter(article__id=article_id)
    # comment_list = article.article_comment.all()
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        # "comment_list" : comment_list,
        "hashtag_list" : hashtag_list,
    }

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        # print(username)
        # print(content)

        Comment.objects.create(
            article=article,
            username=username,
            content=content
        )

        return HttpResponseRedirect("/{}/".format(article_id))

    return render(request, 'detail.html', ctx)


# def about(request):
#     pass
