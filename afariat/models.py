from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Immobilier(models.Model):
    id = models.AutoField(primary_key=True)
    nameImmobilier = models.CharField(max_length=255)
    imageImmobilier = models.TextField(db_column='data',blank=True, null=True)
    priceImmobilier = models.CharField(max_length=255, null=True)
    dateImmobilier = models.CharField(max_length=255, null=True)
    annoceImmobilier = models.CharField(max_length=255, null=True)
    villeImmobilier = models.CharField(max_length=255, null=True)
    activationAnnonce = models.BooleanField(default=False)
    annoceWNScrappOfAdmin = models.BooleanField(default=False)
    idImmobilier = models.ForeignKey('CategorieAnnonce.Categorie', max_length=255, on_delete=models.CASCADE,null=True)
    emailUser = models.ForeignKey(User,on_delete=models.CASCADE)



class Emploi(models.Model):
    id = models.AutoField(primary_key=True)
    nameEmploi = models.CharField(max_length=255)
    imageEmploi = models.TextField(db_column='data',blank=True, null=True)
    priceEmploi = models.CharField(max_length=255, null=True)
    dateEmploi = models.CharField(max_length=255, null=True)
    annoceEmploi = models.CharField(max_length=255, null=True)
    villeEmploi = models.CharField(max_length=255, null=True)
    activationAnnonce = models.BooleanField(default=False)
    annoceWNScrappOfAdmin = models.BooleanField(default=False)
    idEmploi = models.ForeignKey('CategorieAnnonce.Categorie', max_length=255, on_delete=models.CASCADE,null=True)
    emailUser = models.ForeignKey(User,on_delete=models.CASCADE)


class MaterielleInformatique(models.Model):
    id = models.AutoField(primary_key=True)
    nameMatrInformatique = models.CharField(max_length=255)
    imageMatrInformatique = models.TextField(db_column='data',blank=True, null=True)
    priceMatrInformatique = models.CharField(max_length=255, null=True)
    dateMatrInformatique = models.CharField(max_length=255, null=True)
    annoceMatrInformatique = models.CharField(max_length=255, null=True)
    villeMatrInformatique = models.CharField(max_length=255, null=True)
    annoceWNScrappOfAdmin = models.BooleanField(default=False)
    activationAnnonce = models.BooleanField(default=False)
    idMaterielleInformatique = models.ForeignKey('CategorieAnnonce.Categorie', max_length=255, on_delete=models.CASCADE,null=True)
    emailUser = models.ForeignKey(User,on_delete=models.CASCADE)
