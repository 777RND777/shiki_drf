from django.contrib import admin

from . import models


@admin.register(models.Anime)
class AnimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(models.Genre)
admin.site.register(models.Review)
