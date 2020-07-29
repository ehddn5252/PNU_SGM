from django.contrib import admin
from .models import *
# Register your models here.
# admin에 User 모델 추가하기
admin.site.register(User)