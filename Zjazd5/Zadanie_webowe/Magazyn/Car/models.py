from django.db import models
from Engine.models import Engine

# Create your models here.
TYP_NADWOZIA = {
    ('sedan', "Sedan"),
    ('kombi', "Kombi"),
    ('hatchbag', "Hatchbag"),

}


class Car(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    typ_nadwozia = models.CharField(max_length=50, choices=TYP_NADWOZIA, blank=True, null=True)
    rok_produkcji = models.IntegerField()
    engine = models.ForeignKey(Engine, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"(self.marka) | (self.model)"
