from django.urls import path
  
from . import views

urlpatterns = [
   # path('/adopt/', views.
    #path('map/', views.map),
    path('', views.all_squirrels),
    path('<unique_squirrel_id>/', views.update_squirrel),
    path('add/', views.add_squirrel),
    #path('sightings/stats/', views.squirrel_stats),

]
