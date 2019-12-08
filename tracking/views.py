from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'tracking/all.html', context)

    #return HttpResponse(text)

def update_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=squirrel_id)
    if request.method == 'POST':
       form = SquirrelForm(request.POST, instance=squirrel)
       if form.is_valid():
           form.save()
           return redirect(f'/sightings/{squirrel_id}')
        #check data with form
    else:
        form = SquirrelForm(instance=squirrel)
        #build new empty form

    context = {
        'form': form,
    }

    return render(request,'tracking/edit.html', context)



def add_squirrel(request):
    if request.method == 'POST':
       form = SquirrelForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect(f'/sightings/')
        #check data with form
    else:
        form = SquirrelForm()
        #build new empty form

    context = {
        'form': form,
    }

    return render(request,'tracking/edit.html', context)

def squirrel_stats(request):
    #run from human statistic
    squirrel=0
    runs_yes = 0
    runs_no = 0
    total=len(Squirrel.objects.all())
    for squirrel in Squirrel.objects.all():
        if squirrel.runs_from == True:
            runs_yes += 1
        else:
            runs_no += 1
        

    context = {
        'runs_yes': runs_yes,
        'runs_no': runs_no,
    }

    return render(request, 'tracking/stats.html', context)

# Create your views here.
