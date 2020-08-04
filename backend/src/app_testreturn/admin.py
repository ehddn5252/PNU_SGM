from django.contrib import admin
from .models import TestReturn

# Register your models here.

class TestReturnAdmin(admin.ModelAdmin):  
    list_display = (
        'user_name', 
        'stra_name',
        'principal',
        'profit',
        )
 
admin.site.register(TestReturn, TestReturnAdmin)