from rest_framework import serializers
from .models import Movie, Director, MovieActor, Technician

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieActor
        fields = '__all__'

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True, read_only=True)
    actors = MovieActorSerializer(many=True, read_only=True)
    technicians = TechnicianSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'year_of_release', 'rating', 'directors', 'actors', 'technicians']
