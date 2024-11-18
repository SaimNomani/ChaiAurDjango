from django.urls import path, include
from . import views

# defining routes here with views that will handle those routes
urlpatterns = [
    path("", views.all_chai, name='all_chai'), # handling the transfered control from projects urls.py
    
] 