from django.urls import path
  
from . import views

urlpatterns = [
    #path('map/', views.map),
    path('sightings/', views.all_squirrels), 
    path('sightings/add/', views.add_squirrel), 
    path('sightings/stats/', views.squirrel_stats),
    path('sightings/<squirrel_id>/', views.update_squirrel),

]
