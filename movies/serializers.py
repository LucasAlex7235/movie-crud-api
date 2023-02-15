from .models import Rating, Movie, MovieOrder
from rest_framework import serializers
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True)
    rating = serializers.ChoiceField(
        choices=Rating.choices, default=Rating.G
    )
    synopsis = serializers.CharField(allow_null=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, object: Movie):
        return object.added_by.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='movie.title')
    price = serializers.FloatField()
    buyed_by = serializers.ReadOnlyField(source='user.email')
    buyed_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = MovieOrder
        fields = ['id', 'title', 'price', 'buyed_by', 'buyed_at']

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
