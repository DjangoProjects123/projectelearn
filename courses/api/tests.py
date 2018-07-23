# import datetime
# from django.core.urlresolvers import reverse
# from django.test import TestCase
#
#
# class CoursesViewsTestCase(TestCase):
#     # fixtures = ['subjects3.json']
#
#     def test_SubjectListView(self):
#         resp = self.client.get(reverse('subject_list', kwargs={'poll_id': 1}))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_SubjectDetailView(self):
#         resp = self.client.get(reverse('subject_detail'))
#         self.assertEqual(resp.status_code, 200)
