import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from courses.models import Subject, Course


class CoursesViewsTestCase(TestCase):
    # fixtures = ['subjects5.json']

    def test_CourseListView(self):
        resp = self.client.get(reverse('course_list'))
        self.assertEqual(resp.status_code, 200)
        # self.assertTrue('model' in resp.context)
        # self.assertTrue('template_name' in resp.context)
        # self.assertEqual([course.pk for course in resp.context['courses']], [1])


    def test_HomeView(self):
        resp = self.client.get(reverse('course_home'))
        self.assertEqual(resp.status_code, 200)

    def test_ApiCourseView(self):
        resp = self.client.get(reverse('api:subject_list'))
        self.assertEqual(resp.status_code, 200)


class AccountsTestCase(TestCase):
    # fixtures = ['subjects3.json']

    def test_LoginView(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_LogoutDetailView(self):
        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)