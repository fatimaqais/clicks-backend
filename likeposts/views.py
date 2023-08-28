from rest_framework import generics, permissions
from clicks_api.permissions import IsOwnerOrReadOnly
from likeposts.models import LikePost
from likeposts.serializers import LikeSerializer


class LikePostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = LikePost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikePostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = LikePost.objects.all()
