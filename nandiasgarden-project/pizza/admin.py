from django.contrib import admin

from .models import Size, Pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Size)