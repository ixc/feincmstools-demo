from django.contrib import admin
from .models import Meetup

class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("date", "title")}

admin.site.register(Meetup, MeetupAdmin)