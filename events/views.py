from django.http import Http404
from django.db.models import Count
from rest_framework import status, permissions, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
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

    queryset = Events.objects.annotate(
        reviews_count=Count('eventreviews', distinct=True),
        eventlikes_count=Count('likedevent', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'eventlikes_count',
        'reviews_count'
    ]
    filterset_fields = {
        'category': ['exact']
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventsSerializer

    queryset = Events.objects.annotate(
        reviews_count=Count('eventreviews', distinct=True),
        eventlikes_count=Count('likedevent', distinct=True)
    ).order_by('-created_at')
