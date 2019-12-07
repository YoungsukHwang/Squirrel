from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'tracking/all.html', context)

    #return HttpResponse(text)

def squirrel_details(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(id=unique_squirrel_id)
    return HttpResponse(squirrel)


def update_squirrel(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(id=unique_squirrel_id)
    if request.method == 'POST':
       form = SquirrelForm(request.POST, instance=squirrel)
       if form.is_valid():
           form.save()
           return redirect(f'/tracking/{unique_squirrel_id}')
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
           return redirect(f'/tracking/')
        #check data with form
    else:
        form = SquirrelForm()
        #build new empty form

    context = {
        'form': form,
    }

    return render(request,'tracking/edit.html', context)

#def squirrel_stats(request):
# Create your views here.
