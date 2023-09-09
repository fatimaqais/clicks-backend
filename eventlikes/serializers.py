from rest_framework import serializers
from django.db import IntegrityError
from eventlikes.models import LikeEvent


class EventLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeEvent
        fields = ['id', 'created_at', 'owner', 'event']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate like'
            })
