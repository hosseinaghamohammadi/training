from django.urls import path
from . import views

app_name='calorie_counter'
urlpatterns = [
    path('insert', views.home, name='home'),
    path('inserting/', views.insert_item, name='insertion'),
    path('checkNames/', views.get_name, name='namesـquery'),
    
]