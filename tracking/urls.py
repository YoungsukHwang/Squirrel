from django.urls import path
  
from . import views

urlpatterns = [
    #path('/adopt/', views. ),
    #
    path('map/', views.map),
    # ex: /sightings/
    path('sightings/', views.all_squirrels),
    # ex: /sightings/5/
    # ex: /sightings/add/ 
    path('sightings/stats/', views.squirrel_stats),
    path('sightings/add/', views.add_squirrel), 
    path('sightings/<squirrel_id>/', views.update_squirrel),
    # ex: /sightings/stats/

]
