from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
def getData(model, ser):
    # try:
        data = model.objects.all()
        serializer = ser(data, many=True)
        return serializer.data
    # except Exception:
    #     return []


class HomePage(APIView):
    def get(self, req):
        cards = getData(HomeCards, HomeCardsSerializer)
        carouselImage = getData(HomeCarouselImage, HomeCarouselImageSerializer)
        results = getData(HomeResults, HomeResultsSerializer)
        programs = getData(HomePrograms, HomeProgramsSerializer)
        return Response(
            {
                "cards": cards,
                "carouselImage": carouselImage,
                "results": results,
                "programs": programs,
            }
        )


# class AboutPage(APIView):
#     def get(self, req):
#         carouselImage = getData(AboutCarouselImage, AboutCarouselImageSerializer)
#         return Response({"carouselImage": carouselImage})


class CourcePage(APIView):
    def get(self, req):
        cource = getData(Cource, CourceSerializer)
        return Response({"cource": cource})


class TestimonialPage(APIView):
    def get(self, req):
        testimonial = getData(Testimonial, TestimonialSerializer)
        return Response({"testimonial": testimonial})


class ResultsPage(APIView):
    def get(self, req):
        qs_jee = ResultsSection.objects.filter(stream="JEE").order_by("stream","order")
        qs_neet = ResultsSection.objects.filter(stream="NEET").order_by("stream","order")
        jee_results = ResultsSectionSerializer(qs_jee, many=True)
        neet_results = ResultsSectionSerializer(qs_neet, many=True)
        jee_results = jee_results.data
        neet_results = neet_results.data
        aCards = getData(AchievementsCard, AchievementCardSerializer)
        return Response({"jee_results": jee_results,
                         "neet_results": neet_results,
                         "aCards": aCards})


# class ContactForm(APIView):
#     def post(self, req):
#         data = req.data
#         try:
#             Contact.objects.create(
#                 first_name=data.get("firstName", ""),
#                 last_name=data.get("lastName", ""),
#                 email=data.get("email", ""),
#                 message=data.get("message", ""),
#             )
#             return Response({"message": "Form submitted successfully"})
#         except Exception as e:
#             return Response({"message": "Form submission failed"})
