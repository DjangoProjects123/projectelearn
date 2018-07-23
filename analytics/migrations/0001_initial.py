# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course_enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_enrolled', models.DateTimeField(auto_now_add=True)),
                ('course', models.ManyToManyField(related_name='courses', to='courses.Course')),
                ('student', models.ManyToManyField(related_name='courses_enrolled', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_enrolled',),
            },
        ),
        migrations.CreateModel(
            name='course_unenrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_unenrolled', models.DateTimeField(auto_now_add=True)),
                ('course', models.ManyToManyField(related_name='coursesUn', to='courses.Course')),
                ('student', models.ManyToManyField(related_name='courses_unenrolled', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_unenrolled',),
            },
        ),
    ]
