from django.shortcuts import render, HttpResponse

# Create your views here.

from car.models import Car

def cars_list(reqwest):
    Car = Car.objects.all():
    return render()


