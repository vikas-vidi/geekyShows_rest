from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerailizer

# Create your views here.

class Studentapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer
