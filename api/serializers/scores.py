"""Score Serializer"""

# rest_framework
from rest_framework import serializers

# models
from api.models import Score


class ScoreModelSerializer(serializers.ModelSerializer):
    """Score model Serializer"""
    course = serializers.StringRelatedField(read_only=True)
    student = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta class"""
        model = Score
        fields = ('course', 'student',
                  'test_score', 'observations'
                  )
