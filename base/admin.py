__author__ = 'thatcher'


from django.contrib import admin
from django_filepicker.widgets import FPFileWidget
from django import forms

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.sessions.
from django.contrib.sessions.models import Session
from .models import *


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    list_display = ['full_name', 'sort_weight', 'show_as_team']
admin.site.register(TeamMember, TeamMemberAdmin)


class NewsItemAdmin(admin.ModelAdmin):
    model = NewsItem
    list_display = ['id', 'title', 'publication_date', 'show', 'author']
admin.site.register(NewsItem, NewsItemAdmin)


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['title', 'location', 'date_and_time']
admin.site.register(Event, EventAdmin)


class ImageAdmin(admin.ModelAdmin):
    model = Image

    change_form_template = 'admin/filepicker_admin_form.html'

    formfield_overrides = {
        django_filepicker.models.FPFileField: {'widget': FPFileWidget},
        models.CharField: {'widget': forms.Textarea}
    }

    # list_display = ['name']

admin.site.register(Image, ImageAdmin)