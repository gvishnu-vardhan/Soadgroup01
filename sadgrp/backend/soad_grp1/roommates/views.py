from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import roommate_details
from django.shortcuts import render, get_object_or_404, redirect
from .serializers import CreateSerializer

class quotelistapiview(ListAPIView):
    queryset = roommate_details.objects.all()
    serializer_class = CreateSerializer