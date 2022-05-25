
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register("studentapi", views.Studentapi, basename="studentapi")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
]
