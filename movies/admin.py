from django.contrib import admin
from .models import movie, genre
# Register your models here.


class genreadmin(admin.ModelAdmin):
    list_display = ("id", "name")


class movieadmin(admin.ModelAdmin):
    exclude = ("datecreated", )
    list_display = ("id", "title", "genre", "daily_rate")


admin.site.register(genre, genreadmin)
admin.site.register(movie, movieadmin)
