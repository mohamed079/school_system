from django.urls import path
from .views import TeacherView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',TeacherView,basename="teacher_view")
urlpatterns = [
    
]

urlpatterns = urlpatterns + router.urls