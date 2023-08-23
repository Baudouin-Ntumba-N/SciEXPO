from django.contrib import admin
from articles.models import Article, Categorie, Comment, CommentAdmin
admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Categorie)
