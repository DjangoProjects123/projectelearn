# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='/static/images/course_1.jpg', upload_to='course_pics/'),
        ),
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(default='/static/images/course_1.jpg', upload_to='subject_pics/'),
        ),
    ]
