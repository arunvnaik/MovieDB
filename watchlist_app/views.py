# from django.shortcuts import render 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import Movie, Director, MovieActor, Technician
from watchlist_app.serializers import MovieSerializer, DirectorSerializer, MovieActorSerializer, TechnicianSerializer

class MovieListCreateAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DirectorListCreateAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def delete(self, request, pk):
        director = self.get_object(pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieActorListCreateAPIView(APIView):
    def get(self, request):
        actors = MovieActor.objects.all()
        serializer = MovieActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieActorRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return MovieActor.objects.get(pk=pk)
        except MovieActor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        actor = self.get_object(pk)
        serializer = MovieActorSerializer(actor)
        return Response(serializer.data)

    def delete(self, request, pk):
        actor = self.get_object(pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TechnicianListCreateAPIView(APIView):
    def get(self, request):
        technicians = Technician.objects.all()
        serializer = TechnicianSerializer(technicians, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TechnicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnicianRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Technician.objects.get(pk=pk)
        except Technician.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        technician = self.get_object(pk)
        serializer = TechnicianSerializer(technician)
        return Response(serializer.data)

    def delete(self, request, pk):
        technician = self.get_object(pk)
        technician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)