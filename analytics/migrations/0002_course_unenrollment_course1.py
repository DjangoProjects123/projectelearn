# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_unenrollment',
            name='course1',
            field=models.ManyToManyField(related_name='coursesUn1', to='courses.Course'),
        ),
    ]
