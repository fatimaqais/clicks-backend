from rest_framework import generics, permissions
from clicks_api.permissions import IsOwnerOrReadOnly
from eventlikes.models import LikeEvent
from eventlikes.serializers import EventLikeSerializer


class LikeEventList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventLikeSerializer
    queryset = LikeEvent.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeEventDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventLikeSerializer
    queryset = LikeEvent.objects.all()
