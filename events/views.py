from django.http import Http404
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Events
from .serializers import EventsSerializer
from clicks_api.permissions import IsOwnerOrReadOnly


class EventsList(generics.ListCreateAPIView):
    serializer_class = EventsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Events.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventsDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventsSerializer

    def get_object(self, pk):
        try:
            event = Events.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventsSerializer(
            event, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventsSerializer(
            event, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
