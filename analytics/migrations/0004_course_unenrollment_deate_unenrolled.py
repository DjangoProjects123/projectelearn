# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_remove_course_unenrollment_course1'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_unenrollment',
            name='deate_unenrolled',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 22, 8, 54, 17, 480836, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
