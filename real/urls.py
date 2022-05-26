from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('', DetailViewSet,)
router.register('posts', PostViewSet)
router.register('estate', EstateViewSet)
router.register('amentitis',  AmentitisViewSet)

urlpatterns = router.urls
