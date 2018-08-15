from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.AnalyticsListView.as_view(),
        name='analytics_instructor_courses'),
    url(r'^enrollment/$',
        views.AnalyticsEnrollView.as_view(),
        name='analytics_instructor_enrollment'),
     
    url(r'^api/enrollments/$', views.getJson,
        name='api-enrollments-monthly'),
    url(r'^api/enrolls_to_unenrolls/$', views.enrollsTounenrolls,
        name='api-enrolls-unenrolls'),

    # url(r'^api/course/students/$', views.getJson,
    #     name='api-course-students'),     
   

 
]