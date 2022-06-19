from django.db import models

# Create your models here.
class Categorie(models.Model):
    # idUser = models.AutoField(primary_key=True)
    nomCategorie = models.CharField(max_length=255, primary_key=True)
    activationCategorie = models.BooleanField(default=False)