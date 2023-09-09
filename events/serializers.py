from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from events.models import Events
from eventlikes.models import LikeEvent


class EventsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    event_like_id = serializers.SerializerMethodField()
    eventlikes_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 4:
            raise serializers.ValidationError(
                'Image size is larger than 4MB!'
            )
        if value.image.width > 5000:
            raise serializers.ValidationError(
                'Image width larger than 500px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_event_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            eventlike = LikeEvent.objects.filter(
                owner=user, event=obj
            ).first()
            return eventlike.id if eventlike else None
        return None

    class Meta:
        model = Events
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'image', 'details', 'date', 'category',
            'event_like_id', 'eventlikes_count'
        ]
