# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0007_auto_20180722_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_enrollment',
            name='course',
            field=models.ManyToManyField(related_name='courses', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='course_enrollment',
            name='student',
            field=models.ManyToManyField(related_name='courses_enrolled', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course_unenrollment',
            name='course',
            field=models.ManyToManyField(related_name='coursesUn', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='course_unenrollment',
            name='student',
            field=models.ManyToManyField(related_name='courses_unenrolled', to=settings.AUTH_USER_MODEL),
        ),
    ]
