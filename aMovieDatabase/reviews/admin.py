from django.contrib import admin
from .models import Reviewinfo

class ReviewinfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content']

admin.site.register(Reviewinfo, ReviewinfoAdmin)
