from django.contrib import admin
from .models import Module, Course
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import CourseGroup

admin.site.register(Module)



admin.site.unregister(Group)

@admin.register(CourseGroup)
class CustomGroupAdmin(GroupAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'permissions')}),
        (_('Description'), {'fields': ('description',)}),
    )


