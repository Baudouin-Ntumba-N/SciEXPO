from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ["id", "title", "excerpt", "categorie", "author", "content", "photo", "published"]

    widgets = {

        'excerpt': forms.Textarea(attrs={'cols': 25, 'rows':4, 'class':'form-control'}),

        'title': forms.TextInput(attrs={'class':'form-control'}),

    }


class UpdateArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ["id", "title", "excerpt", "categorie", "content", "photo", "published"]

    widgets = {

        'excerpt': forms.Textarea(attrs={'cols': 25, 'rows':4, 'class':'form-control'}),

        'title': forms.TextInput(attrs={'class':'form-control'}),

    }



class ReplyForm(forms.Form):

  reply_content = forms.CharField(widget = forms.TextInput())

  comment_id = forms.CharField(widget = forms.HiddenInput())



class CommentForm(forms.Form):

  #user_id = forms.CharField(widget = forms.HiddenInput())

  article_slug = forms.CharField(widget = forms.HiddenInput())

  comment = forms.CharField(widget = forms.TextInput())