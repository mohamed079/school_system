from django.urls import path
from .views import StudentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',StudentView,basename="student_view")
urlpatterns = [
    
]

urlpatterns = urlpatterns + router.urls