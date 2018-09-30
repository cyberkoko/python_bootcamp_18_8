from django.db import models

# Create your models here.

RODZAJ_SILNIKA = {
    ('disel', "Disel"),
    ('benz', "Benz"),
    ('parowy', "Parowy"),
    ('odrzutowy', "Odrzutiwy"),
    ('inny', "Inny")

}


class Engine(models.Model):

    pojemność = models.IntegerField(null=True, blank=True)
    ilość_cylindrów = models.IntegerField(null=True, blank=True)
    rodzaj = models.CharField(max_length=50, choices=RODZAJ_SILNIKA)



