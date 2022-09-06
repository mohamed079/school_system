from django.urls import path
from .views import ClothesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ClothesView,basename="clothes_view")
urlpatterns = [
    
]

urlpatterns = urlpatterns + router.urls