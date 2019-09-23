from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("addarticle/", views.addArticle, name="addarticle"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("article/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.updateArticle, name="update"),
    path("delete/<int:id>", views.deleteArticle, name="delete"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("confirm/<int:id>", views.confirmArticle, name="confirm"),
    path("unconfirm/<int:id>", views.unconfirmArticle, name="unconfirm"),
    path("viewarticle/<int:id>", views.viewArticle, name="article"),
    path("viewcategory/<int:category>", views.viewCategory, name="category"),
    path("search/", views.searchArticle, name="search"),
    path("viewbyauthor/<int:author_id>", views.viewbyauthor, name="viewbyauthor"),
    path("articlesindex/", views.articlesindex, name="articlesindex"),
]
