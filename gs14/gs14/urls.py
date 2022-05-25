from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentlist", StudentListAndCreate.as_view(), name="studentlist"),
    path("studentlist/<int:pk>", StudentUpdateRetriveDestroy.as_view(), name="studentlist"),
]
