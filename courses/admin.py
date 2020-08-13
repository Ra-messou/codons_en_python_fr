from django.contrib import admin

from .models import Categorie, Video, Text_file,Torrent

# list of imported models
course_models = [Categorie, Video, Text_file,Torrent]

admin.site.register(course_models)
# Register your models here.
