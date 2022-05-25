from .serializer import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication 
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttle import CustomUserThroottle

# Create your views here.
class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_class = [SessionAuthentication]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]     # default throttle
    throttle_classes = [CustomUserThroottle, AnonRateThrottle]     # custom throttle

