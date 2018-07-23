from django.contrib import admin
from .models import Subject, Course, Module
from .forms import SubjectImageForm
# from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    form = SubjectImageForm
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


# @admin.register(MarkdownxModelAdmin)
