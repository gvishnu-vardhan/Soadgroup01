from rest_framework.serializers import ModelSerializer
from .models import roommate_details

class CreateSerializer(ModelSerializer):
    class Meta:
        model = roommate_details
        fields = [
            'user',
            'name',
            'gender',
            'hometown',
            'roomtown',
            'language',
            'occupation',
            'course',
            'alcohol',
            'smoking',
            'culinary',
            'food_preference'
        ]