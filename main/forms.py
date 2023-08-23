from django import forms
from main.models import Inscrit, EtantEleve
from django.utils.translation import gettext_lazy as _


class InscritForm(forms.ModelForm):

    class Meta:
        model = Inscrit

        fields = ['username', 'first_name', 'last_name', 'email', 'school_name',
                  'current_city', 'birth_date', 'function_in_school', 'about', 'password']

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),

            'school_name': forms.Select(attrs={'class': 'form-control'}),

            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),

            'about': forms.Textarea(attrs={'class': 'form-control', 'cols': 20, 'rows': 4, 'placeholder': "Ex: CEO de Turing, Docteur en TIC, ..."}),

            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

        labels = {
            "username": _("Nom d'utilisateur"),
            "first_name": _("Prénom"),
            "last_name": _("Nom"),
            "email": _("Adresse email"),
            "password": _("Mot de passe"),

        }


class EtantEleveForm(forms.ModelForm):

    class Meta:
        model = EtantEleve

        fields = ['eleve', 'classe_del_eleve', 'option', 'tuteur']

        labels = {

            "classe_del_eleve": _("Classe"),
            "tuteur": _("Nom du responsable"),

        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=100, label="Mot de passe",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SettingsForm(forms.ModelForm):

    class Meta:
        model = Inscrit

        fields = ['first_name', 'last_name', 'email', 'school_name', 'current_city',
                  'birth_date', 'function_in_school', 'about', 'photo', 'cover_image']

        widgets = {

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.TextInput(attrs={'class': 'form-control'}),

            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),

            'about': forms.Textarea(attrs={
              'class': 'form-control',
              'placeholder': "Ex: Je suis un passioné de la Tech, PDG de Mulykap, Master en Economie, ...", 'cols': 20, 'rows': 4}),
        }