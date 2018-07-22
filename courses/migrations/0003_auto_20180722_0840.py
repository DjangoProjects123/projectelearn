# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180721_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
