from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from main.models import Inscrit
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField




User = get_user_model()


class Categorie(models.Model):
  nom = models.CharField(max_length=20, null=False, verbose_name='Nom')
  def __str__(self):
    return self.nom
  class Meta:
    verbose_name="Catégorie"



class Article(models.Model):
    title = models.CharField(max_length=100)

    excerpt = models.TextField(blank=True, max_length=500, null=True)

    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    content = RichTextField(blank=True, null=True)

    photo = models.ImageField(upload_to='images', default='images/default_img/carrefour.jpg', null=True)

    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    published = models.BooleanField(default=False)

    likes = models.ManyToManyField(User, related_name="liker")

    def __str__(self):
        return self.title

    #methode save() modifiée
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title) :
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)




class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    comment_content = models.TextField(blank=True, verbose_name='Commentaire')

    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    post_date = models.DateTimeField(auto_now_add=True, null=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def replies(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        else:
            return False

    @property
    def get_replies_number(self):
        return len(Comment.objects.filter(parent = self))

    class Meta:
        verbose_name = "Commentaire"




class CommentAdmin(admin.ModelAdmin):
    list_display=('id', 'writer', 'comment_content', 'commented_article', 'post_date')

    list_filter = ('writer',)

    #read_only = ("post_date")