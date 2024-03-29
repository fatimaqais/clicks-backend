from rest_framework import serializers
from django.db import IntegrityError
from following.models import Following


class FollowingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(
        source='followed.username'
    )

    class Meta:
        model = Following
        fields = ['id', 'owner', 'created_at', 'followed',
                  'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate following'
            })
