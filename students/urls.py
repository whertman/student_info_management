from django.urls import path
from .views import detail_view, delete_view

urlpatterns = [
    path('<id>', detail_view), 
    path('<id>/delete', delete_view),  
]
