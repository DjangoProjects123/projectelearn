# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_auto_20180722_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_enrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course_enrollment',
            name='student',
        ),
        migrations.RemoveField(
            model_name='course_unenrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course_unenrollment',
            name='student',
        ),
    ]
