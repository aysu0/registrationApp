from django.contrib import admin
from .models import Module, Registration
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


admin.site.register(Module)
admin.site.register(Registration)


