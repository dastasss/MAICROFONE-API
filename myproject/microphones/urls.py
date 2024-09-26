# microphones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('neumann/', views.NeumannViewSet.as_view({'get': 'list', 'post': 'create'}), name='neumann-list'),
    path('neumann/<int:pk>/', views.NeumannViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='neumann-detail'),
    path('sennheiser/', views.SennheiserViewSet.as_view({'get': 'list', 'post': 'create'}), name='sennheiser-list'),
    path('sennheiser/<int:pk>/', views.SennheiserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='sennheiser-detail'),
]
