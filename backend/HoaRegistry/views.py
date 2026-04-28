from rest_framework import viewsets
from .models import HoaProfile
from .serializers import HoaProfileSerializer

class HoaProfileViewSet(viewsets.ModelViewSet):
    # Only fetch HOAs that haven't been soft-deleted
    queryset = HoaProfile.objects.filter(is_deleted=False).order_by('-created_at')
    serializer_class = HoaProfileSerializer