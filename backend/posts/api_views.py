from .models import Posts
from .serializers import PostsSerializer
from rest_framework import permissions, viewsets


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-created_at')
    serializer_class = PostsSerializer
    permission_classes = [permissions.AllowAny]
