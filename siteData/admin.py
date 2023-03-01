from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([HomeCarouselImage, HomeCards, HomePrograms, HomeResults, 
                    #  AboutCarouselImage,
                     Cource,
                     Testimonial,
                     AchievementsCard,
                     ResultImage])

# class ResultSectionInline(admin.StackedInline):
#     model = ResultsIndividual
#     extra = 1


# @admin.register(ResultsSection)
# class ResultsSectionAdmin(admin.ModelAdmin):
#     inlines = [ResultSectionInline]


# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'message', 'date_created']

#     def name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

