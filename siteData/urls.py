from django.urls import path
from .views import *

urlpatterns = [
    path("home", HomePage.as_view()),
    path("about", AboutPage.as_view()),
    path("cource", CourcePage.as_view()),
    path("testimonial", TestimonialPage.as_view()),
    path("results", ResultsPage.as_view()),
    # path("contact", ContactForm.as_view()),
]
