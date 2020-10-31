from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import roommate_details
from django.shortcuts import render, get_object_or_404, redirect
from .serializers import CreateSerializer

class quotelistapiview(ListAPIView):
    queryset = roommate_details.objects.all()
    serializer_class = CreateSerializer

def populate(request):
    model = roommate_details.objects.all()
    if request.method == 'POST':
        model = roommate_details()
        model.name = request.POST.get('name')
        model.gender = request.POST.get('gender')
        model.hometown = request.POST.get('hometown')
        model.roomtown = request.POST.get('roomtown')
        model.language = request.POST.get('language')
        model.occupation = request.POST.get('occupation')
        model.course = request.POST.get('course')
        model.alcohol = request.POST.get('alcohol')
        model.smoking = request.POST.get('smoking')
        model.food_preference = request.POST.get('food_preference')
        model.culinary = request.POST.get('culinary')
        model.save()
        return render(request,'home.html')
    else:
        return render(request,'home.html',{'model':model})

class recommendations(ListAPIView):
    serializer_class = CreateSerializer
    queryset = roommate_details.objects.all()
    def filter(self,request,format=None):
        queryset = Listing.objects.all()

        gender_query = request.data.get('gender')
        if gender_query != ' ' and gender_query is not None:
            queryset = queryset.filter(gender__icontains = gender_query)

        hometown_query = request.data.get('hometown')
        if hometown_query != ' ' and hometown_query is not None:
            queryset = queryset.filter(hometown__icontains = hometown_query)

        roomtown_query = request.data.get('roomtown')
        if roomtown_query != ' ' and roomtown_query is not None:
            queryset = queryset.filter(roomtown__icontains = roomtown_query)

        language_query = request.data.get('language')
        if language_query != ' ' and language_query is not None:
            queryset = queryset.filter(language__icontains = language_query)

        occupation_query = request.data.get('occupation')
        if occupation_query != ' ' and occupation_query is not None:
            queryset = queryset.filter(occupation__icontains = occupation_query)

        course_query = request.data.get('course')
        if course_query != ' ' and course_query is not None:
            queryset = queryset.filter(course__icontains = course_query)

        alcohol_query = request.data.get('alcohol')
        if alcohol_query != ' ' and alcohol_query is not None:
            queryset = queryset.filter(alcohol__icontains = alcohol_query)

        smoking_query = request.data.get('smoking')
        if smoking_query != ' ' and smoking_query is not None:
            queryset = queryset.filter(smoking__icontains = smoking_query)

        food_preference_query = request.data.get('food_preference')
        if food_preference_query != ' ' and food_preference_query is not None:
            queryset = queryset.filter(food_preference__icontains = food_preference_query)

        culinary_query = request.data.get('culinary')
        if culinary_query != ' ' and culinary_query is not None:
            queryset = queryset.filter(culinary__icontains = culinary_query)    

        serializer = CreateSerializer(queryset,many = True)
        return Response(serializer.data)


