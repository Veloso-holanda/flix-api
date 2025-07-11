from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenresCreateListView(generics.ListCreateAPIView):
    queryset =  Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer