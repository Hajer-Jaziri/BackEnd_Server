from django.db import models

class Notification(models.Model):
    idNotification = models.AutoField(primary_key=True)
    emailAdmin = models.CharField(max_length=255, null=True)
    emailMembre = models.CharField(max_length=255, null=True)
    contenu = models.CharField(max_length=255, null=True)
    dateNotification = models.DateField(null=True)