# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_remove_course_unenrollment_deate_unenrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_enrollment',
            name='studentName',
            field=models.CharField(max_length=200, default=datetime.datetime(2018, 7, 22, 9, 28, 50, 825671, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course_unenrollment',
            name='studentName',
            field=models.CharField(max_length=200, default=datetime.datetime(2018, 7, 22, 9, 29, 23, 307776, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
