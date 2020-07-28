"""Score Serializer"""

# rest_framework
from rest_framework import serializers

# models
from api.models import Score, Course, Student


class ScoreModelSerializer(serializers.ModelSerializer):
    """Score model Serializer"""
    course = serializers.StringRelatedField(read_only=True)
    student = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta class"""
        model = Score
        fields = ('course', 'student', 'test_score', 'observations')


class AddScoreSerializer(serializers.Serializer):
    """Add score Serializer
        this serializer will handle the request of add scores to
        the courses.
    """
    student_username = serializers.CharField(max_length=100, required=True)
    test_score = serializers.FloatField(max_value=100, required=True)
    observations = serializers.CharField(max_length=200)
    # this will provide by the url in the kwargs
    course_name = serializers.CharField(max_length=100, required=True)

    def validate_course_name(self, data):
        """Validate if the course exists, or is correct"""
        try:
            course = Course.objects.get(slug_name=data, is_active=True)
        except Course.DoesNotExist:
            raise serializers.ValidationError('Invalid Course')
        self.context['course'] = course
        return data

    def validate_student_username(self, data):
        """Validate if the Student exists or is correct"""
        try:
            student = Student.objects.get(username=data, is_active=True)
        except Student.DoesNotExist:
            raise serializers.ValidationError('Invalid Student')
        self.context['student'] = student
        return data

    def validate(self, data):
        """Validate that the student is in the course"""
        course = self.context['course']
        student = self.context['student']
        if not course.students.filter(username=student.username, is_active=True):
            raise serializers.ValidationError('Student is not enrolled the course')
        return data

    def create(self, data):
        """This function allow to add score to the student"""
        course = self.context['course']
        student = self.context['student']
        score = Score.objects.create(student=student,
                                     course=course,
                                     test_score=data['test_score'],
                                     observations=data['observations']
                                     )

        return score
