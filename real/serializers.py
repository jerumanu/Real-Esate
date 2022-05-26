from rest_framework import serializers
from .models import *


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'title', 'detail_descripe', 'photos', 'bedroom_no', 'bathroom_no']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'phone_no','email']


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ['id', 'location', 'price',  'image', 'description']


class AmentitisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amentitis
        fields = ['id', 'security', 'parking','power', 'pool', 'water']




