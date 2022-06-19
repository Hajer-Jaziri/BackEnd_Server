from django.contrib import admin
from .models import Immobilier
from .models import Emploi
from .models import MaterielleInformatique

admin.site.register(Immobilier)
admin.site.register(Emploi)
admin.site.register(MaterielleInformatique)

# Register your models here.
