"""Courses Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Course, Student


# Seralizer


class CoursesModelSerializer(serializers.ModelSerializer):
    """Course model serialzier"""
    grade_name = serializers.StringRelatedField(read_only=True, source='grade')
    teacher_name = serializers.StringRelatedField(read_only=True, source='teacher')
    students = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        """Meta Courses"""
        model = Course
        fields = (
            'slug_name', 'name', 'description', 'grade', 'grade_name',
            'is_limited', 'student_limit', 'schedule', 'teacher', 'teacher_name',
            'students'
        )
        extra_kwargs = {
            'is_limited': {'required': True},
            'student_limit': {'required': True},
            'schedule': {'required': True},
            'description': {'required': True},
            'grade': {'write_only': True},
            'teacher': {'write_only': True}
        }


class AssignSerializer(serializers.Serializer):
    """Assign Serializer
    """
    course = serializers.CharField(max_length=100, required=True)
    student_username = serializers.CharField(max_length=100, required=True)

    def validate_course(self, data):
        """Validate if the course exists, or is correcct"""
        try:
            course = Course.objects.get(slug_name=data)
        except Course.DoesNotExist:
            raise serializers.ValidationError('Invalid Course')
        self.context['course'] = course
        return data

    def validate_student_username(self, data):
        """Validate if the Student exists or is correct"""
        try:
            student = Student.objects.get(username=data)
        except Student.DoesNotExist:
            raise serializers.ValidationError('Invalid Student')
        self.context['student'] = student
        return data

    def validate(self, data):
        """Validate:
            -if the course is in the grade level of the student
            -if the student has been assigned in the course
        """
        course = self.context['course']
        student = self.context['student']
        # verify if the student is in the same grade level that the course required
        if student.grade != course.grade:
            raise serializers.ValidationError('Student can not be assigned,'
                                              'this course is not for his grade level')
        # verify if the student is not in the course
        if course.students.filter(username=student.username).exists():
            raise serializers.ValidationError('Student is already assign')
        # Verify is the course is capable of add new student
        if course.is_limited and course.students.count() >= course.student_limit:
            raise serializers.ValidationError('Course has reached its member limit')
        return data

    def create(self, data):
        """Assign the Student into the course"""
        course = self.context['course']
        student = self.context['student']
        course.students.add(student)
        course.save()
        return student
