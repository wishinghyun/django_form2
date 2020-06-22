from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        # form.is_valid()  ==>  form이 유효한지 판단하여 true, false 리턴
        if form.is_valid():
            # article = Article.objects.get(pk=pk)
            # form에 담긴 정보가 ArticleForm이고
            # ArticleForm은 Article의 정보를 가지고 있다
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method =="POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    #print(request.resolver_match.url_name) #url 이름 리턴
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)