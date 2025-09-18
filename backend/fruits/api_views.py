from .models import Fruits
from .serializers import FruitsSerializer
from rest_framework import permissions, viewsets


class FruitsViewSet(viewsets.ModelViewSet):
    queryset = Fruits.objects.all().order_by('-created_at')
    serializer_class = FruitsSerializer
    permission_classes = [permissions.IsAuthenticated]
