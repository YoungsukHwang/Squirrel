from django.http import HttpResponse
from django.shortcuts import render

from .models import Squirrel


def all_squirrels(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'adopt/all.html', context)

    #return HttpResponse(text)

def squirrel_details(request, squirrel_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)

def update_squirrel(request, squirrel_id):

def add_squirrel(request):

def squirrel_stats(request):
# Create your views here.
