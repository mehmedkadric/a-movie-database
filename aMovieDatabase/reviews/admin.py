from django.contrib import admin
from .models import Reviewinfo, ReviewImage

class ReviewinfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content']

class ReviewImageAdmin(admin.ModelAdmin):
        list_display = ('movie', 'image', 'caption')


admin.site.register(Reviewinfo, ReviewinfoAdmin)
admin.site.register(ReviewImage, ReviewImageAdmin)

