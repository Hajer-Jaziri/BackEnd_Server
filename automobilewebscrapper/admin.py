from django.contrib import admin
from .models import Marque
from .models import AnnonceVoiture
from .models import VoitureNeuf
from .models import VoitureOccasion

admin.site.register(Marque)
admin.site.register(AnnonceVoiture)
admin.site.register(VoitureNeuf)
admin.site.register(VoitureOccasion)

# Register your models here.
