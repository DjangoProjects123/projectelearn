# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('studentName', models.CharField(max_length=200)),
                ('date_enrolled', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_enrolled',),
            },
        ),
        migrations.CreateModel(
            name='course_unenrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('studentName', models.CharField(max_length=200)),
                ('date_unenrolled', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_unenrolled',),
            },
        ),
    ]
