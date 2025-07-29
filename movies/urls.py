from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveiUpdateDestroyView, MovieStatsView



urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>', MovieRetrieveiUpdateDestroyView.as_view(), name='movie-detail-update-delete'),
    path('movies/stats', MovieStatsView.as_view(), name='moview-stats')
]
