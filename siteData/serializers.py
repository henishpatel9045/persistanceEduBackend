from rest_framework import serializers
from .models import (
    HomeCards,
    HomeCarouselImage,
    HomePrograms,
    HomeResults,
    # AboutCarouselImage,
    Cource,
    Testimonial,
    AchievementsCard,
    ResultsIndividual,
    ResultsSection,
)


class HomeCarouselImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        return obj.image.url

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
        fields = (
            "title",
            "desc",
        )


# class AboutCarouselImageSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()
#     def get_image(self, obj):
#         return obj.image.url

#     class Meta:
#         model = AboutCarouselImage
#         fields = ("image",)


class CourceSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = Cource
        fields = (
            "title",
            "image",
            "content",
        )

    def get_content(self, obj):
        return [obj.para1, obj.para2]


class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        print(obj.image.url)
        return obj.image.url

    class Meta:
        model = Testimonial
        fields = (
            "image",
            "name",
            "subtitle",
            "content",
        )


class AchievementCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementsCard
        fields = ("title",)


# class ResultImageSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()
#     def get_image(self, obj):
#         return obj.image.url
    
#     class Meta:
#         model = ResultImage
#         fields = ("title", "subtitle", "image",)


class ResultsIndividualSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = ResultsIndividual
        fields = (
            "image",
            "name",
            "title",
            "subtitle",
        )


class ResultsSectionSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = ResultsSection
        fields = (
            "title",
            "subtitle",
            "data",
        )

    def get_data(self, obj):
        results = ResultsIndividual.objects.filter(section=obj)
        serializer = ResultsIndividualSerializer(results, many=True)
        return serializer.data
