from django.contrib import admin
from .models import Profile, Langage

class LangageAdmin(admin.ModelAdmin):
    list_display = ["titre", "slug", "description"]
    list_display_links = ["titre", ]
    prepopulated_fields = {'slug': ('titre',)}


admin.site.register(Profile)
admin.site.register(Langage, LangageAdmin)
# Register your models here.
