from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


from .models import Squirrel
from .forms import SquirrelForm



def map(request):
    squirrels = Squirrel.objects.order_by()[0:100]
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'tracking/map.html', context)

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
    runs_yes = 0
    runs_no = 0
    for squirrel in Squirrel.objects.all():
        if squirrel.runs_from == True:
            runs_yes += 1
        else:
            runs_no += 1

    #location of first sighting
    Above_Ground = 0
    Ground_Plane = 0
    for squirrel in Squirrel.objects.all():
        if squirrel.location == 'Above Ground':
            Above_Ground += 1
        elif squirrel.location == 'Ground Plane':
            Ground_Plane += 1

    chase_yes = 0
    chase_no = 0
    for squirrel in Squirrel.objects.all():
        if squirrel.chasing == True:
            chase_yes += 1
        else:
            chase_no += 1

    moans_yes = 0
    moans_no = 0
    for squirrel in Squirrel.objects.all():
        if squirrel.moans == True:
            moans_yes += 1
        else:
            moans_no += 1

    kuks_yes = 0
    kuks_no = 0
    for squirrel in Squirrel.objects.all():
        if squirrel.kuks == True:
            kuks_yes += 1
        else:
            kuks_no += 1

    context = {
        'runs_yes': runs_yes,
        'runs_no': runs_no,
        'Above_Ground':  Above_Ground,
        'Ground_Plane': Ground_Plane,
        'chase_yes': chase_yes,
        'chase_no': chase_no,
        'moans_yes': moans_yes,
        'moans_no': moans_no,
        'kuks_yes': kuks_yes,
        'kuks_no': kuks_no,
    }

    return render(request, 'tracking/stats.html', context)

# Create your views here.
