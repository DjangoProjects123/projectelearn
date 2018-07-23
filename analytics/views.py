from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic import TemplateView
from django.forms.models import modelform_factory
from django.apps import apps
from django.db.models import Count
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin 
from courses.models import Course, Module, Content, Subject
from django.core.cache import cache
from django.contrib.auth.models import User
from .models import course_enrollment, course_unenrollment
from datetime import date
import datetime
from django.views.generic import View
from django.http import JsonResponse
import json

 


# Create your views here.
 
class AnalyticsListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'analytics/analytics.html'     

    def get(self, request ):
        subjects = cache.get('all_subjects')

        #get the date of the request
        dateNow = datetime.datetime.now()

        #date requested by the lecturer
        #dateRequested = year

        if not subjects:
            subjects = Subject.objects.annotate(total_courses=Count('courses'))
            cache.set('all_subjects', subjects)
        courses = cache.get('all_courses')
        all_courses_enrolls = course_enrollment.objects.filter(date_enrolled__year = dateNow.year).filter(course__owner_id = self.request.user.id)
        all_courses_enrolls = course_enrollment.objects.annotate(total_enrolls= Count('date_enrolled')) 
        all_courses_unenrolls = course_unenrollment.objects.filter(date_unenrolled__year = dateNow.year).filter(course__owner_id = self.request.user.id)
        all_courses_unenrolls = course_unenrollment.objects.annotate(total_unenrolls =Count('date_unenrolled'))
     
        all_courses = Course.objects.annotate(total_students=Count('students')).filter(owner_id = self.request.user.id) 

        if not courses:
            courses = all_courses 
            cache.set('all_courses', courses) 
                    
        return self.render_to_response({'subjects': subjects, 
                                        'courses': courses,
                                        'all_courses_enrolls': all_courses_enrolls,
                                        'all_courses_unenrolls':all_courses_unenrolls
                                        })


class AnalyticsEnrollView(TemplateResponseMixin, View):
    model = Course
    template_name = 'analytics/analyticsEnrollment.html'     

    def get(self, request ):
        subjects = cache.get('all_subjects')

        #get the date of the request
        dateNow = datetime.datetime.now()

        #date requested by the lecturer
        #dateRequested = year

        if not subjects:
            subjects = Subject.objects.annotate(total_courses=Count('courses'))
            cache.set('all_subjects', subjects)
 
        all_courses = Course.objects.annotate(total_students=Count('students')).filter(owner_id = self.request.user.id)        
        courses = cache.get('all_courses')
        if not courses:
            courses = all_courses 
            cache.set('all_courses', courses)

        #query all of the enrollments filtered by the date today or arguments date
        all_enrolls = course_enrollment.objects.filter(date_enrolled__year = dateNow.year).filter(course__owner_id = self.request.user.id)
        instructor_courses = Course.objects.filter( owner = self.request.user)
        labels_y = []
        data_x = []
        data_xx = []

        for course in instructor_courses:
            labels_y.append(course.title)
            for i in range(0,12):
                mon = i+1
                all_enrolls_final = all_enrolls.filter(course__exact = course, date_enrolled__month = mon)
                total_enrolls = all_enrolls_final.count()

                data_xx.append(total_enrolls)
            data_x.append(data_xx)

            labelDict = dict([i, labels_y[labels_y.index(i)]] for i in labels_y)
           # dateDict = dict([i, data_x[data_x.index(i)]] for i in data_x)
 
        return self.render_to_response({'labelDict': labelDict, 
                                        'data_x': data_x,
                                          
                                        })
