from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, filters
from clicks_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        events_count=Count('owner__events', distinct=True),
        following_count=Count('owner__following', distinct=True),
        followed_count=Count('owner__followed', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
    ]
    ordering_fields = [
        'posts_count',
        'events_count',
        'followed_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        events_count=Count('owner__events', distinct=True),
        followed_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
