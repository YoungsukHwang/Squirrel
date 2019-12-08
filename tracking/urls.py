from django.urls import path
  
from . import views

urlpatterns = [
    #path('map/', views.map),
    path('sightings/', views.all_squirrels),
    path('sightings/<unique_squirrel_id>/', views.update_squirrel),
    path('sightings/add/', views.add_squirrel),
    #path('sightings/stats/', views.squirrel_stats),

]
