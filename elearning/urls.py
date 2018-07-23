"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
from courses.views import CourseHomeView, CourseListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^$', CourseHomeView.as_view(), name='course_home'),
    url(r'^allcourses/$', CourseListView.as_view(), name='course_list'),
    url(r'^students/', include('students.urls')),
    url(r'^api/', include('courses.api.urls', namespace='api')),
    url(r'search/', include('haystack.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
