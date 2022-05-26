from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('details',DetailViewSet.as_view(), name='details'),
    path('posts', PostViewSet.as_view(), name='posts'),
    path('descriptions', EstateViewSet.as_view(), name='descriptions'),
    path('amentitis', AmentitisViewSet.as_view(), name='amentitis'),
]
