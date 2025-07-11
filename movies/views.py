from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerialize


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialize


class MovieRetrieveiUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialize