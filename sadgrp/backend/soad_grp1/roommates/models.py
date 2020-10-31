from django.db import models
from accounts.models import User
# Create your models here.
gender_choice = (
    ('male','MALE'),
    ('female','FEMALE'),
    ('non-binary','NON-BINARY')
)
habit_choice=(
    ('yes','YES'),
    ('flexible','FLEXIBLE'),
    ('no','NO')
)
skill_choice=(
    ('can','CAN'),
    ('sometimes','SOMETIMES'),
    ('cannot','CANNOT')
)
food_choice=(
    ('flexible','Flexible'),
    ('strictly veg','Strictly Veg'),
    ('strictly non veg','Strictly Non Veg')
)
class roommate_details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    gender = models.CharField(max_length=20,choices=gender_choice)
    hometown = models.CharField(max_length=264)
    roomtown = models.CharField(max_length=264)
    language = models.CharField(max_length=264)
    occupation = models.CharField(max_length=264)
    course = models.CharField(max_length=264)
    alcohol = models.CharField(max_length=20,choices=habit_choice)
    smoking = models.CharField(max_length=20,choices=habit_choice)
    food_preference = models.CharField(max_length=20,choices=food_choice)
    culinary = models.CharField(max_length=20,choices=skill_choice)