from rest_framework import generics, permissions
from clicks_api.permissions import IsOwnerOrReadOnly
from .models import Following
from .serializers import FollowingSerializer


class FollowingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
