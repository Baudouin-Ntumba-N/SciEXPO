from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

class About(models.Model):
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/ABOUT_US', null=True)

    def __str__(self):
        return str(self.id)+" A PROPOS DE NOUS"

    class Meta:
        verbose_name = "À propos de nous"


class Ecole(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Inscrit(AbstractUser):
    class FunctionInSchool(models.TextChoices):
        ELEVE = 'Eleve', _('Elève')
        PROFESSOR = 'Professeur', _('Professeur')
        DIRECTEUR = 'Directeur', _('Directeur')
        PREFET = 'Prefet', _('Préfet')
        SECRETAIRE = 'Secretaire', _('Secretaire')
        ANCIEN_ELEVE = 'Ancien_eleve', _('Ancien élève')
        DEFAULT = '-', _('-')

    function_in_school = models.CharField(
        max_length=40,
        choices=FunctionInSchool.choices,
        default=FunctionInSchool.DEFAULT,
        verbose_name='Statut'
    )

    school_name = models.ForeignKey(Ecole, on_delete=models.SET_NULL, null=True)

    current_city = models.CharField(max_length=20, null=True, verbose_name="Ville ou territoire actuel(le)")

    birth_date = models.DateField(null=True, verbose_name="Date de naissance")

    about = models.TextField(null=True, blank=True, verbose_name="A propos de vous")

    photo = models.ImageField(upload_to = 'photos', default='photos/default.jpg')

    cover_image = models.ImageField(upload_to = 'images',
                                    default='images/default_img/cover_default.jpg',
                                   verbose_name="Image de couverture")



class Option(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class EtantEleve(models.Model):
    eleve = models.OneToOneField(Inscrit, on_delete=models.CASCADE)
    class ClasseEleve(models.TextChoices):
        SEPTIEME = '7emeEB', _('7e EB')
        HUITIEME = '8emeEB', _('8e EB')
        PREMIERE = '1ere', _('1ère des Humanités')
        DEUXIEME = '2eme', _('2ème des Humanités')
        TROISIEME = '3eme', _('3ème des Humanités')
        QUATRIEME = '4eme', _('4ème des Humanités')
        DEFAULT = '-', _('-')

    classe_del_eleve = models.CharField(
        max_length=30,
        choices=ClasseEleve.choices,
        default=ClasseEleve.DEFAULT,
        verbose_name="classe de l'élève")

    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, null=True, blank=True)

    tuteur = models.CharField(max_length=30)

    def __str__(self):
        return self.eleve.first_name+" "+self.eleve.last_name+", "+self.eleve.school_name.nom


    class Meta:
        verbose_name = "Élève"