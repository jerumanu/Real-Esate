from django.shortcuts import render
from rest_framework import viewsets # new



from .models import *
from .serializers import *
# Create your views here.


class DetailViewSet(viewsets.ModelViewSet):  # new


   
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    

class PostViewSet(viewsets.ModelViewSet):  # new

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EstateViewSet(viewsets.ModelViewSet):  # new

    queryset = Estate.objects.all()
    serializer_class = EstateSerializer


class AmentitisViewSet(viewsets.ModelViewSet):  # new

    queryset =Amentitis.objects.all()
    serializer_class =AmentitisSerializer
