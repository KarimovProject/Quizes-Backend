from django.contrib import admin
from .models import Quiz, Question,Topic, Option, User, Result, Result_detail
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Option)
admin.site.register(User)
admin.site.register(Result)
admin.site.register(Result_detail)
