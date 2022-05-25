from rest_framework.throttling import UserRateThrottle

class CustomUserThroottle(UserRateThrottle):
    scope = 'custom'