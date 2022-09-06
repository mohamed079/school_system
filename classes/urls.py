from django.urls import path
from .views import ClassesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ClassesView,basename="Class_View")
urlpatterns = [
    
]

urlpatterns = urlpatterns + router.urls