import datetime
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from courses.models import Subject, Course


class CoursesViewsTestCase(TestCase):
    fixtures = ['subjects3.json']

    def test_CourseListView(self):
        resp = self.client.get(reverse_lazy('course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('model' in resp.context)
        self.assertTrue('template_name' in resp.context)
        self.assertEqual([course.pk for course in resp.context['courses']], [1])