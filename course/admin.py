from django.contrib import admin
from .models import Modules, Sections, Lessons

# Register your models here.
admin.site.register(Modules)
admin.site.register(Sections)
admin.site.register(Lessons)