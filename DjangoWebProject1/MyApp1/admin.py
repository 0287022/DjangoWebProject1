from django.contrib import admin
from .models import teacher, courseDescription, courseArea

# Register your models here.
admin.site.register(teacher)
admin.site.register(courseArea)
admin.site.register(courseDescription)