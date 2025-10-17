from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Tarea
from .serializers import TareaSerializer

class SmallPagination(PageNumberPagination):
    page_size = 5

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-created_at')
    serializer_class = TareaSerializer
    pagination_class = SmallPagination
