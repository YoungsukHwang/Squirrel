from django.urls import path
  
from . import views

urlpatterns = [
    #path('/adopt/', views. ),
    #
    path('map', views.map),
    # ex: /sightings/
    path('', views.all_squirrels),
    # ex: /sightings/5/
    path('<int:unique_squirrel_id>/', views.update_squirrel),
    # ex: /sightings/add/
    path('sightings/add/', views.add_squirrel),
    # ex: /sightings/stats/
    #path('sightings/stats/', views.squirrel_stats),

]
