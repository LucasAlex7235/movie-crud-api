from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework import serializers
from django.shortcuts import render
from .models import Movie, MovieOrder
from accounts.models import Account
from datetime import datetime
import ipdb


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        user = request.user
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(added_by=user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieViewDetail(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        user = request.user
        serializerOrder = MovieOrderSerializer(data=request.data)
        serializerOrder.is_valid(raise_exception=True)
        serializerOrder.save(user=user, movie=movie)
        return Response(serializerOrder.data, status=status.HTTP_201_CREATED)
