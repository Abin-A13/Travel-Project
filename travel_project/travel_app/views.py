from django.shortcuts import render
from .models import Place, Person


# Create your views here.
def scr_print(request):
    obj = Place.objects.all()
    person = Person.objects.all()
    return render(request, "index.html", {'area': obj, 'team': person})
