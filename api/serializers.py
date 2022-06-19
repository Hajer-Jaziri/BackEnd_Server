from rest_framework import serializers
from automobilewebscrapper.models import Marque, VoitureNeuf, VoitureOccasion, AnnonceVoiture
from afariat.models import Immobilier,Emploi, MaterielleInformatique
from CategorieAnnonce.models import Categorie
from Notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
       model = Notification
       fields = '__all__'

class AnnonceVoitureSerializer(serializers.ModelSerializer):
    class Meta:
       model = AnnonceVoiture
       fields = '__all__'

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
       model = Marque
       fields = '__all__'

class VoitureNeufSerializer(serializers.ModelSerializer):
    class Meta:
       model = VoitureNeuf
       fields = '__all__'

# class VendeurProSerializer(serializers.ModelSerializer):
#     class Meta:
#        model = VendeurPro
#        fields = '__all__'

class VoitureOccasionSerializer(serializers.ModelSerializer):
    class Meta:
       model = VoitureOccasion
       fields = '__all__'


# class ConcessionnairesSerializer(serializers.ModelSerializer):
#     class Meta:
#        model = Concessionnaires
#        fields = '__all__'

class ImmobilierSerializer(serializers.ModelSerializer):
    class Meta:
       model = Immobilier
       fields = '__all__'

class EmploiSerializer(serializers.ModelSerializer):
    class Meta:
       model = Emploi
       fields = '__all__'

class MaterielleInformatiqueSerializer(serializers.ModelSerializer):
    class Meta:
       model = MaterielleInformatique
       fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
       model = Categorie
       fields = '__all__'