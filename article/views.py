from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.forms import modelformset_factory
from .models import categories
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    articles = Article.objects.all()[:10]
    return render(request, "index.html", {"articles": articles})


def about(request):
    articles = Article.objects.all()[:10]
    return render(request, "about.html", {"articles": articles})

def contact(request):
    articles = Article.objects.all()[:10]
    return render(request, "contact.html", {"articles": articles})

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale Başarıyla Oluşturuldu")
        return redirect(reverse("article:detail", kwargs={"id": article.id}))

    return render(request, "addarticle.html", {"form": form})


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }

    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "detail.html", {"article": article})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.isConfirmed = False
        article.save()

        messages.success(request, "Makale Başarıyla Güncellendi")
        return redirect(reverse("article:detail", kwargs={"id": article.id}))

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi")
    return redirect("article:dashboard")


@login_required(login_url="user:login")
def confirmation(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }

    return render(request, "confirmation.html", context)


@login_required(login_url="user:login")
def confirmArticle(request, id):
    user = request.user
    group = str(Group.objects.get(user=user))

    if group == "Admin" or group == "Editör":
        article = get_object_or_404(Article, id=id)
        article.isConfirmed = True
        article.save()
        messages.success(request, "Makale Onaylandı")
        return redirect("article:confirmation")
    else:
        messages.warning(request, "Kullanıcı İzniniz Bulunmamakta")
        return render(request, "index.html")

@login_required(login_url="user:login")
def unconfirmArticle(request, id):
    user = request.user
    group = str(Group.objects.get(user=user))

    if group == "Admin" or group == "Editör":
        article = get_object_or_404(Article, id=id)
        article.isConfirmed = False
        article.save()
        messages.warning(request, "Makale Onayı Geri Alındı")
        return redirect("article:confirmation")
    else:
        messages.warning(request, "Kullanıcı İzniniz Bulunmamakta")
        return render(request, "index.html")


def viewArticle(request, id):
    article = get_object_or_404(Article, id=id)
    all_articles = Article.objects.all()[:10]
    return render(request, "viewarticle.html", {"articles": all_articles, "article": article})


def viewCategory(request, category):
    articles_category = Article.objects.filter(category=category)[:20]
    all_articles = Article.objects.all()[:10]
    return render(request, "viewcategory.html", {"articles": all_articles, "articles_category": articles_category})


def viewbyauthor(request, author_id):
    author_name = str(list(User.objects.filter(id=author_id))[0])
    authors_artciles = Article.objects.filter(author_id=author_id)
    all_articles = Article.objects.all()[:10]
    return render(request, "categorybyauthor.html", {"articles": all_articles, "authors_artciles": authors_artciles, "author_name": author_name})


def searchArticle(request):
    pass


def articlesindex(request):
    all_articles = Article.objects.all().order_by('id')
    return render(request, "articlesindex.html", {"articles": all_articles})