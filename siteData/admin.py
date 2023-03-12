from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([HomeCarouselImage, HomeCards, HomePrograms, HomeResults, 
                    #  AboutCarouselImage,
                     Cource,
                     Testimonial,
                     AchievementsCard,])

class ResultSectionInline(admin.StackedInline):
    model = ResultsIndividual
    extra = 1


@admin.register(ResultsSection)
class ResultsSectionAdmin(admin.ModelAdmin):
    inlines = [ResultSectionInline]
    list_display = ['title', 'order', ]
    list_editable = ["order",]
    ordering = ["order",]


# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'message', 'date_created']

#     def name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

