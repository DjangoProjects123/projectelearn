from django import forms
from django.forms.models import inlineformset_factory
from django.http import HttpResponse, HttpResponseForbidden

from .models import Course, Module, Subject
from django.core.files.images import get_image_dimensions


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True)


class SubjectImageForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data['image']

        try:
            w, h = get_image_dimensions(image)

            # validate dimensions
            max_height = 700
            max_width = 700
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            min_height = 300
            min_width = 400
            if w < min_width or h < min_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or larger.' % (min_width, min_height))

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(image) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new image
            """
            pass

        return image


class CourseImageForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data['image']

        try:
            w, h = get_image_dimensions(image)

            # validate dimensions
            max_height = 700
            max_width = 700
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            min_height = 500
            min_width = 400
            if w < min_width or h < min_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or larger.' % (min_width, min_height))

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(image) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new image
            """
            pass

        return image


