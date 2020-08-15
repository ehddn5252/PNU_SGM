from django.contrib import admin

# Register your models here.

from .models import User, Stretagy, Result

admin.site.register(User)
admin.site.register(Stretagy)
admin.site.register(Result)