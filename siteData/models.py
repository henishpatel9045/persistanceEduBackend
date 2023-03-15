from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

# Create your models here.

class HomeCarouselImage(models.Model):
    image = CloudinaryField("image")

    def __str__(self):
        return str(self.pk)


class HomeCards(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
    

class HomeResults(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class HomePrograms(models.Model):
    title = models.CharField(max_length=800)
    desc = models.TextField()

    def __str__(self):
        return self.title

# -------------------------------- ABOUT PAGE -------------------------------- #


# class AboutCarouselImage(models.Model):
#     image = CloudinaryField("image")

#     def __str__(self):
#         return self.title


# -------------------------------- COURCE PAGE ------------------------------- #


class Cource(models.Model):
    title = models.CharField(max_length=1500)
    image = CloudinaryField("image")
    para1 = models.TextField()
    para2 = models.TextField()

    def __str__(self):
        return self.title


# ------------------------------- TESTIMONIALS ------------------------------- #

class Testimonial(models.Model):
    image = CloudinaryField("image")
    name = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.name


# ----------------------------- ACHIEVEMENT PAGE ----------------------------- #

class AchievementsCard(models.Model):
    title = models.CharField(max_length=2500)

    def __str__(self):
        return self.title

# class ResultImage(models.Model):
#     title = models.CharField(max_length=1500)
#     subtitle = models.CharField(max_length=2500, default="", null=True, blank=True)
#     image = CloudinaryField("image")


class ResultsSection(models.Model):
    STREAM = [
        ("JEE", "JEE"),
        ("NEET", "NEET"),
    ]
    
    title = models.CharField(max_length=1500)
    subtitle = models.CharField(max_length=2500, null=True, blank=True)
    stream = models.CharField(choices=STREAM, default='JEE', max_length=30)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1, "Order starts from 1.")])

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['stream', 'order',]


class ResultsIndividual(models.Model):
    section = models.ForeignKey(ResultsSection, on_delete=models.CASCADE)
    image = CloudinaryField("image", blank=True, null=True)
    name = models.CharField(max_length=250)
    collegeName = models.CharField(max_length=250, null=True, blank=True, default="")
    phone = models.CharField(max_length=250, null=True, blank=True, default="")
    order = models.IntegerField(default=1, validators=[MinValueValidator(1, "Order starts from 1.")])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order',]

# # ------------------------------- CONTACT PAGE ------------------------------- #

# class Contact(models.Model):
#     first_name = models.CharField(max_length=250, null=True, blank=True)
#     last_name = models.CharField(max_length=250, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     message = models.TextField(null=True, blank=True)
#     seen = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.pk

#     class Meta:
#         ordering = ('-date_created', )
