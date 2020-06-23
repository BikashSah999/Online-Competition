from django.contrib import admin
from .models import Category, AddCompetition, PhotoContest, StoryContest
# Register your models here.
admin.site.register(Category)
admin.site.register(AddCompetition)
admin.site.register(PhotoContest)
admin.site.register(StoryContest)