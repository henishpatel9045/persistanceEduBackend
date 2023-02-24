from rest_framework import serializers
from .models import (
    HomeCards,
    HomeCarouselImage,
    HomePrograms,
    HomeResults,
    AboutCarouselImage,
    Cource,
    Testimonial,
    AchievementsCard,
    ResultsIndividual,
    ResultsSection,
)


class HomeCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCarouselImage
        fields = ("image",)

class HomeCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCards
        fields = ("title",)

class HomeResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeResults
        fields = ("title",)


class HomeProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePrograms
        fields = ("title", "desc",)


class AboutCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCarouselImage
        fields = ("image",)


class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cource
        fields = ("title", "image", "para1", "para2",)


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class AchievementCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementsCard
        fields = ("title",)


class ResultsIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsIndividual
        fields = ("image", "name", "title", "subtitle",)


class ResultsSectionSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()
    
    class Meta:
        model = ResultsSection
        fields = ("title", "desc", "data",)

    def get_data(self, obj):
        results = ResultsIndividual.objects.filter(section=obj)
        serializer = ResultsIndividualSerializer(results, many=True)
        return serializer.data
    
