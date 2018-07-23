from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.AnalyticsListView.as_view(),
        name='analytics_instructor_courses'),
    url(r'^enrollment/$',
        views.AnalyticsEnrollView.as_view(),
        name='analytics_instructor_enrollment'),
     

        
]