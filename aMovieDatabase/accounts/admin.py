from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    def top_genres_display(self, obj):
        return ', '.join([genre.name for genre in obj.top_genres.all()])
    top_genres_display.short_description = 'Top Genres'

    list_display = ['username', 'email', 'date_of_birth', 'top_genres_display']
    list_filter = ['top_genres']

admin.site.register(User, UserAdmin)
