from django.contrib import admin
from feincmstools.admin import FeinCMSDocumentAdmin
from .models import Meetup

class MeetupAdmin(FeinCMSDocumentAdmin):
    prepopulated_fields = {"slug": ("date", "title")}

admin.site.register(Meetup, MeetupAdmin)