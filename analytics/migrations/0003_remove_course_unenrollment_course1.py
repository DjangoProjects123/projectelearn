# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_course_unenrollment_course1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_unenrollment',
            name='course1',
        ),
    ]
