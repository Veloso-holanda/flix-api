from rest_framework import serializers
from movies.models import Movie


class MovieSerialize(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'