from django.contrib import admin
from .models import Movies, Genre, Theatre
# Register your models here.

admin.site.register(Movies)
admin.site.register(Genre)
admin.site.register(Theatre)