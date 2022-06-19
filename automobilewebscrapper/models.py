from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Marque(models.Model):
    nomMarque = models.CharField(max_length=100, primary_key=True)
    imageMarque = models.TextField(db_column='data',blank=True,null=True)

class AnnonceVoiture(models.Model):
    idVoiture = models.ForeignKey('CategorieAnnonce.Categorie', max_length=255, on_delete=models.CASCADE)
    nomMarque = models.ForeignKey('Marque', max_length=100, on_delete=models.CASCADE,null=True)
    nomVoiture  = models.CharField(max_length=255,null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    image = models.TextField(db_column='data',blank=True,null=True)
    activationAnnonce = models.BooleanField(default=False)
    annoceWNScrappOfAdmin = models.BooleanField(default=False)
    emailUser = models.ForeignKey(User,on_delete=models.CASCADE)
    typeCar = models.CharField(max_length=255,null=True)

class VoitureNeuf(models.Model):
    annonceVoiture = models.ForeignKey('AnnonceVoiture', max_length=255, on_delete=models.CASCADE, primary_key=True)
    disponible = models.CharField(max_length=255, null=True)


class VoitureOccasion(models.Model):
    annonceVoiture = models.ForeignKey('AnnonceVoiture', max_length=255, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=1000,null=True)
    annee = models.CharField(max_length=4,null=True)
    KMS = models.IntegerField(null=True)
    localite = models.CharField(max_length=255,null=True)
    energie = models.CharField(max_length=255,null=True)
    boiteVitesse = models.CharField(max_length=255,null=True)



# class VendeurPro(models.Model):
#     id = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=255,null=True)
#     Tel = models.CharField(max_length=50,null=True)
#     Fax = models.CharField(max_length=50,null=True)
#     image = models.TextField(db_column='data',blank=True,null=True)
#     nomVendeur = models.CharField(max_length=255,null=True)

# class Concessionnaires(models.Model):
#     id = models.AutoField(primary_key=True)
#     nomConcessionnaires = models.CharField(max_length=255,null=True)
#     Tel = models.CharField(max_length=255,null=True)
