from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

'''
# for globaly rest api filter configuration in settings.py
# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['city']
'''
# for locally rest api filter configuration without any seetings.py configuration
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']