from django.urls import path
from genres.views import GenresCreateListView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('genres/', GenresCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-update-delete'),
]