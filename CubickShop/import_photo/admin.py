from django.contrib import admin

from .models import Products_Photo


@admin.register(Products_Photo)
class CategoryAdmin(admin.ModelAdmin):
    pass
