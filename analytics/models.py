from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# Create your models here.
class course_enrollment(models.Model):
    student = models.ManyToManyField(User, related_name='courses_enrolled')
    course = models.ManyToManyField(Course, related_name='courses')
    studentName = models.CharField(max_length=200)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_enrolled',)
     

class course_unenrollment(models.Model):
    student = models.ManyToManyField(User, related_name='courses_unenrolled')
    course = models.ManyToManyField(Course, related_name='coursesUn')
    studentName = models.CharField(max_length=200)
    date_unenrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_unenrolled',)
     