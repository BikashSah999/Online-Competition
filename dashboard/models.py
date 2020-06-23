from django.db import models
from datetime import date , timedelta
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, blank=False, null=False)
    added_by = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return (self.category)

class AddCompetition(models.Model):
    title = models.CharField(max_length=100)
    image  = models.ImageField(upload_to = 'competition/competition_post_images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    added_date = models.DateField(default = date.today)
    deadline = models.DateField(default= date.today() + timedelta(days=1))
    added_by = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name='added_by')
    prize = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class PhotoContest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_user')
    caption = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to = 'competition/photo_contest')
    post_date = models.DateField(default = date.today)
    photo_contest_name = models.ForeignKey(AddCompetition, on_delete=models.SET_NULL, null=True, related_name='photo_contest_name')
    likes = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class StoryContest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_user')
    title = models.CharField(max_length=100, blank=False, null=False)
    story = models.CharField(max_length=10000, blank=False, null=False)
    post_date = models.DateField(default = date.today)
    story_contest_name = models.ForeignKey(AddCompetition, on_delete=models.SET_NULL, null=True, related_name='story_contest_name')
    likes = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title