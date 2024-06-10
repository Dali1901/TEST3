from django.contrib import admin
from .models import Informe

# Register your models here.
class InformeAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','editado')

admin.site.register(Informe, InformeAdmin)