from django.contrib import admin

from .models import CA, Epi, EpiTipo

# Register your models here.

admin.site.register(CA)
admin.site.register(Epi)
admin.site.register(EpiTipo)
