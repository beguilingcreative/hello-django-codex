from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.utilities, name='utilities'),
    path('panic/', views.panic_records, name='panic_records'),
    path('tetris/', views.tetris, name='tetris'),
    path('dino/', views.dino, name='dino'),
]
