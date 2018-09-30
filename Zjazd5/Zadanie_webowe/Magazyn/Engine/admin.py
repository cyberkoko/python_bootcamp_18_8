from django.contrib import admin
from Engine.models import Engine


# Register your models here.
# admin.register(admin.ModelAdmin):
class EngineAdmin(admin.ModelAdmin):
    list_display = ("pojemność","ilość_cylindrów", "rodzaj")

admin.site.register (Engine, EngineAdmin)





