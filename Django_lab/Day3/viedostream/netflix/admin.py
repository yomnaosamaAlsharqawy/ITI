from django.contrib import admin

from .models import Movies, Categories


class MovieInline(admin.StackedInline):
    model = Movies
    extra = 1
    max_num = 10


class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "overview", "year")
    list_filter = ("year",)


admin.site.register(Movies, MovieAdmin)
admin.site.register(Categories)
