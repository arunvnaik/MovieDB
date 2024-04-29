from django.urls import path
from watchlist_app.views import (
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    DirectorListCreateAPIView,
    DirectorRetrieveUpdateDestroyAPIView,
    MovieActorListCreateAPIView,
    MovieActorRetrieveUpdateDestroyAPIView,
    TechnicianListCreateAPIView,
    TechnicianRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),

    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view(), name='director-detail'),

    path('actors/', MovieActorListCreateAPIView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', MovieActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail'),

    path('technicians/', TechnicianListCreateAPIView.as_view(), name='technician-list'),
    path('technicians/<int:pk>/', TechnicianRetrieveUpdateDestroyAPIView.as_view(), name='technician-detail'),
]
