from django.contrib import admin

# Import Classes From Page Models
from .models import *  # noqa: F403
# Register your models here.
admin.site.register(Book)  # noqa: F405
admin.site.register(Category)  # noqa: F405