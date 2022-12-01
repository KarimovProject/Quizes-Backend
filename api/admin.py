from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Quizes, Subject

# Register your models here.

admin.site.register(User)
admin.site.register(Quizes)
admin.site.register(Subject)
