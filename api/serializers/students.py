"""Students Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    """Student Serializer"""

    class Meta:
        """Met class Student"""
        model = Student
        fields = ['username', 'first_name', 'last_name', 'grade',
                  'parents', 'annotations']



'''
class StudentCoursesSerializer(serializers.Serializer):
    """Student Serializer
    """
    student_username = serializers.CharField(max_length=100, required=True)

    def validate_student_username(self, data):
        """Validate if the Student exists or is correct"""
        try:
            student = Student.objects.get(username=data, is_active=True)
        except Student.DoesNotExist:
            raise serializers.ValidationError('Invalid Student')
        self.context['student'] = student
        return data
'''

