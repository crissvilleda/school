"""Courses Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Course, Student, Score

""" 
 This two validators will be used twice, in order to keep the code clear they will be here
 they will be use in:
 --AssignSerializer
 --AddScoreSerializer
"""


# ------------start here
def validate_course(data):
    """Validate if the course exists, or is correct"""
    try:
        course = Course.objects.get(slug_name=data, is_active=True)
    except Course.DoesNotExist:
        raise serializers.ValidationError('Invalid Course')
    return course


def validate_student(data):
    """Validate if the Student exists or is correct"""
    try:
        student = Student.objects.get(username=data, is_active=True)
    except Student.DoesNotExist:
        raise serializers.ValidationError('Invalid Student')
    return student


# -------------end here

class CoursesModelSerializer(serializers.ModelSerializer):
    """Course model serialzier"""
    grade_name = serializers.StringRelatedField(read_only=True, source='grade')
    teacher_name = serializers.StringRelatedField(read_only=True, source='teacher')
    students = serializers.StringRelatedField(many=True, read_only=True)

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
    course_name = serializers.CharField(max_length=100, required=True)
    student_username = serializers.CharField(max_length=100, required=True)

    def validate_course_name(self, data):
        """Validate if the course exists, or is correcct"""
        self.context['course'] = validate_course(data)
        return data

    def validate_student_username(self, data):
        """Validate if the Student exists or is correct"""
        self.context['student'] = validate_student(data)
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


class AddScoreSerializer(serializers.Serializer):
    """Add score Serializer
        this serializer will handle the request of add scores to
        the courses.
    """
    student_username = serializers.CharField(max_length=100, required=True)
    test_score = serializers.FloatField(max_value=100, required=True)
    observations = serializers.CharField(max_length=200)
    # this will provide by the url
    course_name = serializers.CharField(max_length=100, required=True)

    def validate_course_name(self, data):
        """Validate if the course exists, or is correcct"""
        self.context['course'] = validate_course(data)

        return data

    def validate_student_username(self, data):
        """Validate if the Student exists or is correct"""
        self.context['student'] = validate_student(data)
        return data

    def validate(self, data):
        """Validate that the student is in the course"""
        course = self.context['course']
        student = self.context['student']
        if not course.students.filter(username=student.username):
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
