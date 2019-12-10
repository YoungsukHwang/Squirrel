from django.urls import path
  
from . import views

urlpatterns = [
    # ex: /map/
    path('map/', views.map),
    # ex: /sightings/
    path('sightings/', views.all_squirrels),
    # ex: /sightings/stats/
    path('sightings/stats/', views.squirrel_stats),
    # ex: /sightings/add/ 
    path('sightings/add/', views.add_squirrel), 
    # ex: /sightings/5/
    path('sightings/<squirrel_id>/', views.update_squirrel),

]
