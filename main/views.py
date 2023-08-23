from django.shortcuts import render, redirect
from main.forms import InscritForm, EtantEleveForm, LoginForm, SettingsForm
from articles.models import Article
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.paginator import Paginator
from .models import About, Inscrit
from django.views import View
from django.contrib import messages

User = get_user_model()

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    return redirect("login")

  articles = Article.objects.all().order_by('-pub_date')
  #top_article = articles.first()

  page = Paginator(articles, 3)
  pagenumber = request.GET.get('page')
  thispage = page.get_page(pagenumber)

  return render(request, 'main/index.html', {"page": thispage})

def about_us_view(request):
    about = About.objects.get(pk = 1)
    return render(request, 'main/about_us.html', {"about_us": about})
def signup(request):
  form = InscritForm()
  if request.method == "POST":
    f = InscritForm(request.POST)
    if f.is_valid():
      username = f.cleaned_data['username']
      first_name = f.cleaned_data['first_name']
      last_name = f.cleaned_data['last_name']
      email = f.cleaned_data['email']
      current_city = f.cleaned_data['current_city']
      birth_date = f.cleaned_data['birth_date']
      function_in_school = f.cleaned_data['function_in_school']
      password = f.cleaned_data['password']
      school_name = f.cleaned_data['school_name']

      user = User.objects.create_user(
          username = username,
          first_name = first_name,
          last_name = last_name,
          email = email,
          current_city = current_city,
          birth_date = birth_date,
          password = password,
          school_name = school_name,
          function_in_school = function_in_school

      )
      if function_in_school == "Eleve":
            form = EtantEleveForm()
            return render(request, 'main/etant_eleve.html', {"form":form, "eleve":user})
      login_form = LoginForm()
      return render(request, 'main/login.html', {'msg':f'{first_name}, votre compte a été créé avec succès !', 'form':login_form})

    return render(request, 'main/signup.html')

  return render(request, 'main/signup.html', {'form':form})

def etant_eleve(request):
    if request.method == "POST":
        form = EtantEleveForm(request.POST)
        eleve = request.POST["eleve"]
        user = User.objects.get(pk=int(eleve))
        if form.is_valid():
            form.save()
            return render(request, 'main/login.html', {'msg':f'{user.first_name}, votre compte a été créé avec succès!', 'form':LoginForm()})
        else:
            render(request, 'main/etant_eleve.html', {"form":form, 'eleve':user})
class LoginView(View):
    form = LoginForm()
    def get(self,request, *args, **kwargs):
        return render(request, 'main/login.html', {"form":self.form})

    def post(self, request, *args, **kwargs):
        f = LoginForm(request.POST)
        if f.is_valid():
            user = authenticate(username=f.cleaned_data['username'], password=f.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect("home")
            return render(request, "main/login.html", {"form":f, "error":"Nom d'utilisateur ou mot de passe incorrects!"})
        return redirect("login")

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    return redirect("login")


class Settings(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
        	return redirect("login")
        form = SettingsForm(instance=request.user)
        return render(request, "main/settings.html", {"form":form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
        	return redirect("login")
        form = SettingsForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Modifications enregistrées avec succès!")
            return redirect("settings")
        return redirect("settings")


def user_profile(request, username):
    try:
        user = Inscrit.objects.get(username=username)
    except KeyError:
        return redirect("home")
    articles = Article.objects.filter(author = user)
    context = {
               "username":user.get_username(),
               "cover_image":user.cover_image.url,
               "photo": user.photo.url,
               "first_name": user.first_name,
               "last_name":user.last_name,
               "statut": user.function_in_school,
               "ecole": user.school_name,
               "about":user.about,
               "articles": articles,
              }

    return render(request, 'main/user_profile.html', context)



def user_photo_full(request, username):
    try:
        user = Inscrit.objects.get(username=username)
    except KeyError:
        return redirect("home")
    context = {
               "username":user.get_username(),
               "photo": user.photo.url,
               "first_name": user.first_name,
               "last_name":user.last_name,
              }

    return render(request, 'main/user_photo_full.html', context)
