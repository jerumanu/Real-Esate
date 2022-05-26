from django.contrib.auth.models import User
from .serializers import RegisterSerializer
 

from rest_framework import viewsets ,generics # new
from .serializers import MyTokenObtainPairSerializer
# from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *
# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    # queryset = User.objects.all()
    serializer_class = MyTokenObtainPairSerializer




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer




