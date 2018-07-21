from __future__ import absolute_import, division, print_function, unicode_literals

import datetime
from courses.models import Course
from haystack import indexes

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/search/product_search.txt")
    title = indexes.CharField(model_attr='title')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte= datetime.datetime.now())