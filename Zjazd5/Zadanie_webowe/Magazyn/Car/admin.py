
from django.contrib import admin
from Car.models import Car


# Register your models here.
# admin.register(admin.ModelAdmin):
class CarAdmin(admin.ModelAdmin):
    list_display = ("marka","model", "typ_nadwozia","rok_produkcji","engine")

admin.site.register (Car, CarAdmin)

